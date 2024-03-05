import os
import cv2
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import numpy as np

outputImgFolder = 'images/'

pathsWithSamePhotos = [
    '/home/jean-pierre/scratch/20201117_rotated/1pi2/labeled_20201117_1pi2_c3',
    '/home/jean-pierre/scratch/20201117_rotated/2pi4/labeled_20201117_2pi4_c1',
    '/home/jean-pierre/scratch/20201117_rotated/3SamsungGalaxyA5/labeled_20201117_3SamsungGalaxyA4_OC',
    '/home/jean-pierre/scratch/20201117_rotated/4XiaomiRedmi4X/labeled_20201117_4XiaomiRedmi4X_OC',
    '/home/jean-pierre/scratch/20201119_rotated/1XiaomiRedmi4X/labeled_20201119_1XiaomiRedmi4X_OC',
    '/home/jean-pierre/scratch/20201119_rotated/2pi2/labeled_20201119_2pi2_c3',
    '/home/jean-pierre/scratch/20201119_rotated/3pi4/labeled_20201119_3pi4_c3',
    '/home/jean-pierre/scratch/20201119_rotated/4SamsungGalaxyA5_sampled/labeled_20201119_4SamsungGalaxyA_OC_sampled',
    '/home/jean-pierre/scratch/20201126_rotated/3XiaomiRedmi2_sampled/labeled_20201126_3XiaomiRedmi2_OC2_sampled',
    '/home/jean-pierre/scratch/20201126_rotated/4pi4_c4_sampled/labeled_20201126_4pi4_c4_sampled',
    '/home/jean-pierre/scratch/20201126_rotated/4pi4_c5/labeled_20201126_4pi4_c5',
    '/home/jean-pierre/scratch/20201127_rotated/2pi4/labeled_20201127_2pi4_c2',
    '/home/jean-pierre/scratch/20201203_rotated/1pi4_sampled/labeled_20201203_1pi4_c20_sampled',
    '/home/jean-pierre/scratch/20201203_rotated/3pi2/labeled_20201203_3pi2_c4',
    '/home/jean-pierre/scratch/20201203_rotated/4SamsungGalaxyA5/labeled_20201203_4SamsungGalaxyA5_OC',
    '/home/jean-pierre/scratch/unilyon_and_others/20071123_0756_Ain1/labeled_20071123_0756_Ain1',
    '/home/jean-pierre/scratch/unilyon_and_others/20071123_0956_Ain2/labeled_20071123_0956_Ain2',
    '/home/jean-pierre/scratch/unilyon_and_others/20191125_Allier1/labeled_20191125_Allier1',
    '/home/jean-pierre/scratch/unilyon_and_others/20191223_Allier2/labeled_20191223_Allier2'
]

pathsWithDifferingPhotos = [
    '/home/jean-pierre/scratch/unilyon_and_others/randomWoodImages/labeled_2022_randomWoodImages',

    '/home/jean-pierre/scratch/internetVideos/north_creek_2_plus_trabuco_creek'
]

txtsFolder = 'txts'

dflist = []

for path in pathsWithSamePhotos:
    firstFile = True
    shape = [0,0,0]

    imcount = 0
    count = 0
    txtsPath = os.path.join(path,txtsFolder)

    if path == '/home/jean-pierre/scratch/unilyon_and_others/randomWoodImages/labeled_2022_randomWoodImages' or '/home/jean-pierre/scratch/internetVideos/north_creek_2_plus_trabuco_creek':
        for file in os.listdir(txtsPath):
            imcount = imcount + 1
            if file[-4:] == ".txt":
                im = cv2.imread(os.path.join(txtsPath,file).replace('txt','jpg'))
                shape = im.shape
                print(shape)
                Ysize = shape[0]
                Xsize = shape[1]

    for file in os.listdir(txtsPath):
        imcount = imcount + 1
        if file[-4:] == ".txt":
            if firstFile == True:
                im = cv2.imread(os.path.join(txtsPath,file).replace('txt','jpg'))
                shape = im.shape
                print(shape)
                Ysize = shape[0]
                Xsize = shape[1]
                firstFile = False
            with open(os.path.join(txtsPath,file)) as f:
                lines = f.readlines()
                for line in lines:
                    splitted = line.split(' ')
                    if splitted[0] == '0':
                        count = count + 1
                        dflist.append(
                            {
                                'dataset': path.split('/')[-1],
                                'Xax' : Xsize,
                                'Yax' : Ysize,
                                'XcenterBBox': round(float(splitted[1])*Xsize),
                                'YcenterBBox': round(float(splitted[2])*Ysize),
                                'widthBBox' : round(float(splitted[3])*Xsize),
                                'heightBBox' : round(float(splitted[4].split('\n')[0])*Ysize)
                            }
                        )
    print(str(count)+' samples   and   '+str(imcount)+'   images->   '+path)

df = pd.DataFrame(dflist)

df['surfaceBBox'] = df['widthBBox'] * df['heightBBox']
df['SQRTsurfaceBBox'] = np.sqrt(df['widthBBox'] * df['heightBBox'])

print(df)

data1 = df[df['dataset']=='labeled_20201117_1pi2_c3']

print(data1)

features = [
    'XcenterBBox',
    'YcenterBBox',
    'widthBBox',
    'heightBBox',
    'surfaceBBox'
]


feature = 'SQRTsurfaceBBox'
dataset = path.split('/')[-1]
data = df[df['dataset']==dataset]
sb.set(rc={"figure.figsize":(13, 5)}) #width=6, height=5
fig = sb.boxplot(df,x='SQRTsurfaceBBox',y='dataset').get_figure()
fig.tight_layout()
plt.xlim(0, 1100)
#sb.set(rc={"figure.figsize":(13, 4)}) #width=3, #height=4
fig.savefig(outputImgFolder+'boxplot_'+dataset+'_'+feature+'.png', dpi=200)
plt.cla()
plt.clf()
plt.close()

df['relativeYcenterBBox'] = df['YcenterBBox'] / df['Yax']

feature = 'relativeYcenterBBox'
dataset = path.split('/')[-1]
data = df[df['dataset']==dataset]
sb.set(rc={"figure.figsize":(13, 5)}) #width=6, height=5
fig = sb.boxplot(df,x='relativeYcenterBBox',y='dataset').get_figure()
fig.tight_layout()
#plt.xlim(0, 1100)
#sb.set(rc={"figure.figsize":(13, 4)}) #width=3, #height=4
fig.savefig(outputImgFolder+'boxplot_'+dataset+'_'+feature+'.png', dpi=200)

plt.cla()
plt.clf()
plt.close()

df['relativeXcenterBBox'] = df['XcenterBBox'] / df['Xax']

feature = 'relativeXcenterBBox'
dataset = path.split('/')[-1]
data = df[df['dataset']==dataset]
sb.set(rc={"figure.figsize":(13, 5)}) #width=6, height=5
fig = sb.boxplot(df,x='relativeXcenterBBox',y='dataset').get_figure()
fig.tight_layout()
#plt.xlim(0, 1100)
#sb.set(rc={"figure.figsize":(13, 4)}) #width=3, #height=4
fig.savefig(outputImgFolder+'boxplot_'+dataset+'_'+feature+'.png', dpi=200)

'''

for feature in features:
    for path in pathsWithSamePhotos:
        dataset = path.split('/')[-1]

        data = df[df['dataset']==dataset]
        print(data)
        fig = sb.displot(data[feature],kde=True)
        fig.savefig(outputImgFolder+'displot_'+dataset+'_'+feature+'.png')

'''
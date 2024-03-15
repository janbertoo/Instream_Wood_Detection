import os
import cv2
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import numpy as np
import pickle
sb.set_style('white')
outputImgFolder = 'images/'

dataset_number_mapping = {'A': 1, 'B': 2, 'C': 3}

database_base_path = '/home/jean-pierre/scratch/'

paths = [
    database_base_path+'20201117_rotated/1pi2/labeled_20201117_1pi2_c3',
    database_base_path+'20201117_rotated/2pi4/labeled_20201117_2pi4_c1',
    database_base_path+'20201117_rotated/3SamsungGalaxyA5/labeled_20201117_3SamsungGalaxyA4_OC',
    database_base_path+'20201117_rotated/4XiaomiRedmi4X/labeled_20201117_4XiaomiRedmi4X_OC',
    database_base_path+'20201119_rotated/1XiaomiRedmi4X/labeled_20201119_1XiaomiRedmi4X_OC',
    database_base_path+'20201119_rotated/2pi2/labeled_20201119_2pi2_c3',
    database_base_path+'20201119_rotated/3pi4/labeled_20201119_3pi4_c3',
    database_base_path+'20201119_rotated/4SamsungGalaxyA5_sampled/labeled_20201119_4SamsungGalaxyA_OC_sampled',
    database_base_path+'20201126_rotated/3XiaomiRedmi2_sampled/labeled_20201126_3XiaomiRedmi2_OC2_sampled',
    database_base_path+'20201126_rotated/4pi4_c4_sampled/labeled_20201126_4pi4_c4_sampled',
    database_base_path+'20201126_rotated/4pi4_c5/labeled_20201126_4pi4_c5',
    database_base_path+'20201127_rotated/2pi4/labeled_20201127_2pi4_c2',
    database_base_path+'20201203_rotated/1pi4_sampled/labeled_20201203_1pi4_c20_sampled',
    database_base_path+'20201203_rotated/3pi2/labeled_20201203_3pi2_c4',
    database_base_path+'20201203_rotated/4SamsungGalaxyA5/labeled_20201203_4SamsungGalaxyA5_OC',
    database_base_path+'unilyon_and_others/20071123_0756_Ain1/labeled_20071123_0756_Ain1',
    database_base_path+'unilyon_and_others/20071123_0956_Ain2/labeled_20071123_0956_Ain2',
    database_base_path+'unilyon_and_others/20191125_Allier1/labeled_20191125_Allier1',
    database_base_path+'unilyon_and_others/20191223_Allier2/labeled_20191223_Allier2',
    database_base_path+'unilyon_and_others/randomWoodImages/labeled_2022_randomWoodImages'
    database_base_path+'internetVideos/canada_del_oro/labeled_2022_canada_del_oro',
    database_base_path+'internetVideos/hikuwai_river_NZ/labeled_2023_hikuwai_river_NZ',
    database_base_path+'internetVideos/ilfis_river/labeled_2022_ilfis_river',
    database_base_path+'internetVideos/north_creek/labeled_20180802_north_creek',
    database_base_path+'internetVideos/north_creek_2_plus_trabuco_creek/labeled_2022_north_creek_2_plus_trabuco_creek',
    database_base_path+'internetVideos/north_creek_3/labeled_2022_north_creek_3',
    database_base_path+'internetVideos/piha_valley_Auckland/labeled_piha_valley_Auckland',
    database_base_path+'internetVideos/rio_moquegua/labeled_20190205_rio_moquegua',
    database_base_path+'internetVideos/sihl_a_studen/labeled_2022_sihl_a_studen',
    database_base_path+'extra_own_data/20220520_rhone_data/labeled_20220520_rhone_data',
    database_base_path+'extra_own_data/VDN_vid_20210509_174821/labeled_VDN_vid_20210509_174821',
    database_base_path+'extra_own_data/VDN_vid_20210509_180320/labeled_VDN_vid_20210509_180320',
    database_base_path+'extra_own_data/dry_wood_data_VDN_2021/labeled_dry_wood_data_VDN_2021',
    database_base_path+'extra_own_data/dry_wood_data_VDN_2022/labeled_dry_wood_data_VDN_2022'
]


dataset_text_mapping = {
    'labeled_20201117_1pi2_c3' : '1',
    'labeled_20201117_2pi4_c1' : '2',
    'labeled_20201117_3SamsungGalaxyA4_OC' : '3',
    'labeled_20201117_4XiaomiRedmi4X_OC' : '4',
    'labeled_20201119_1XiaomiRedmi4X_OC' : '5',
    'labeled_20201119_2pi2_c3' : '6',
    'labeled_20201119_3pi4_c3' : '7',
    'labeled_20201119_4SamsungGalaxyA_OC_sampled' : '8',
    'labeled_20201126_3XiaomiRedmi2_OC2_sampled' : '9',
    'labeled_20201126_4pi4_c4_sampled' : '10',
    'labeled_20201126_4pi4_c5' : '11',
    'labeled_20201127_2pi4_c2' : '12',
    'labeled_20201203_1pi4_c20_sampled' : '13',
    'labeled_20201203_3pi2_c4' : '14',
    'labeled_20201203_4SamsungGalaxyA5_OC' : '15',
    'labeled_20071123_0756_Ain1' : '16',
    'labeled_20071123_0956_Ain2' : '17',
    'labeled_20191125_Allier1' : '18',
    'labeled_20191223_Allier2' : '19',
    'labeled_2022_randomWoodImages' : '20',
    'labeled_2022_canada_del_oro' : 'A 1',
    'labeled_2022_ilfis_river' : 'A 2',
    'labeled_20180802_north_creek' : 'A 3',
    'labeled_2022_north_creek_2_plus_trabuco_creek' : 'A 4',
    'labeled_2022_north_creek_3' : 'A 5',
    'labeled_20190205_rio_moquegua' : 'A 6',
    'labeled_2022_sihl_a_studen' : 'A 7',
    'labeled_20220520_rhone_data' : 'A 8',
    'labeled_VDN_vid_20210509_174821' : 'A 9',
    'labeled_VDN_vid_20210509_180320' : 'A 10',
    'labeled_dry_wood_data_VDN_2021' : 'D 1',
    'labeled_dry_wood_data_VDN_2022' : 'D 2'
}

if os.path.exists('dataframeAllBBoxes.pkl') == False:

    txtsFolder = 'txts'

    dflist = []

    for path in paths:
        print(path)
        firstFile = True
        shape = [0,0,0]

        imcount = 0
        count = 0
        txtsPath = os.path.join(path,txtsFolder)
        
        #for the following 2 datasets, the image size are not the same throughout the dataset
        if path.endswith('labeled_2022_randomWoodImages') ==True or path.endswith('north_creek_2_plus_trabuco_creek') == True or path.endswith('labeled_dry_wood_data_VDN_2021') == True or path.endswith('labeled_dry_wood_data_VDN_2022') == True:
            print('has different images!')
            for file in os.listdir(txtsPath):
                imcount = imcount + 1
                if file[-4:] == ".txt":
                    im = cv2.imread(os.path.join(txtsPath,file).replace('txt','jpg'))
                    shape = im.shape
                    #print(shape)
                    Ysize = shape[0]
                    Xsize = shape[1]
                with open(os.path.join(txtsPath,file)) as f:
                    lines = f.readlines()
                    for line in lines:
                        splitted = line.split(' ')
                        if splitted[0] == '0':
                            count = count + 1
                            dflist.append(
                                {
                                    'dataset': (path.split('/')[-1]),#.split('_')[1]+'_'+(path.split('/')[-1]).split('_')[2],
                                    'Xax' : Xsize,
                                    'Yax' : Ysize,
                                    'XcenterBBox': round(float(splitted[1])*Xsize),
                                    'YcenterBBox': round(float(splitted[2])*Ysize),
                                    'widthBBox' : round(float(splitted[3])*Xsize),
                                    'heightBBox' : round(float(splitted[4].split('\n')[0])*Ysize)
                                }
                            )
            continue
        
        for file in os.listdir(txtsPath):
            imcount = imcount + 1
            if file[-4:] == ".txt":
                if firstFile == True:
                    im = cv2.imread(os.path.join(txtsPath,file).replace('txt','jpg'))
                    shape = im.shape
                    #print(shape)
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
                                    #'dataset': path.split('/')[-1],
                                    'dataset': (path.split('/')[-1]),#.split('_')[1]+'_'+(path.split('/')[-1]).split('_')[2],                                    
                                    'Xax' : Xsize,
                                    'Yax' : Ysize,
                                    'XcenterBBox': round(float(splitted[1])*Xsize),
                                    'YcenterBBox': round(float(splitted[2])*Ysize),
                                    'widthBBox' : round(float(splitted[3])*Xsize),
                                    'heightBBox' : round(float(splitted[4].split('\n')[0])*Ysize)
                                }
                            )
        print(str(count)+' samples   and   '+str(imcount)+'   images->   '+path)
        #print(dflist)

    df = pd.DataFrame(dflist)

    df.to_pickle('dataframeAllBBoxes.pkl')
else:
    df = pd.read_pickle('dataframeAllBBoxes.pkl')

df['dataset_text'] = df['dataset'].map(dataset_text_mapping)

print(df)

df['surfaceBBox'] = df['widthBBox'] * df['heightBBox']

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

df['SQRTsurfaceBBox'] = np.sqrt(df['widthBBox'] * df['heightBBox'])

feature = 'SQRTsurfaceBBox'
#dataset = path.split('/')[-1]
#data = df[df['dataset']==dataset]
sb.set(rc={"figure.figsize":(13, 5)}) #width=6, height=5
fig = sb.boxplot(df,x='SQRTsurfaceBBox',y='dataset').get_figure()
fig.tight_layout()
plt.xlim(0, 1100)
#sb.set(rc={"figure.figsize":(13, 4)}) #width=3, #height=4
fig.savefig(outputImgFolder+'boxplot_'+feature+'.png', dpi=200)
plt.cla()
plt.clf()
plt.close()


df['relativeSizeBBox'] = (df['widthBBox'] * df['heightBBox']) / (df['Xax'] * df['Yax'])

feature = 'relativeSizeBBox'
#dataset = path.split('/')[-1]
#data = df[df['dataset']==dataset]
sb.set(rc={"figure.figsize":(13, 5)}) #width=6, height=5
fig = sb.boxplot(df,x='relativeSizeBBox',y='dataset').get_figure()
fig.tight_layout()
plt.xlim(0, 0.3)
#sb.set(rc={"figure.figsize":(13, 4)}) #width=3, #height=4
fig.savefig(outputImgFolder+'boxplot_'+feature+'.png', dpi=200)
plt.cla()
plt.clf()
plt.close()





df['SQRTrelativeSizeBBox'] = np.sqrt(df['relativeSizeBBox'])

feature = 'SQRTrelativeSizeBBox'
#dataset = path.split('/')[-1]
#data = df[df['dataset']==dataset]
sb.set(rc={"figure.figsize":(13, 5)}) #width=6, height=5
fig, ax = plt.subplots()
sb.boxplot(df,x='SQRTrelativeSizeBBox',y='dataset_text', ax=ax, color='gray').get_figure()
fig.tight_layout()
#sb.set(rc={"figure.figsize":(13, 4)}) #width=3, #height=4
# Set X-axis label
ax.set_xlabel('Square Root of Relative Size of the Bounding Box')

# Set Y-axis label
ax.set_ylabel('Dataset Number')
# Set tick positions and label positions to 'left'
#ax.yaxis.set_ticks_position('left')
#ax.yaxis.set_label_position('left')
# Align tick labels on the left
#ax.tick_params(axis='y', labelleft=True)
plt.xlim(0, 0.7)

fig.savefig(outputImgFolder+'boxplot_'+feature+'.png', dpi=200)
fig.savefig(outputImgFolder+'boxplot_'+feature+'.svg')
plt.cla()
plt.clf()
plt.close()









df['relativeYcenterBBox'] = df['YcenterBBox'] / df['Yax']

feature = 'relativeYcenterBBox'
#dataset = path.split('/')[-1]
#data = df[df['dataset']==dataset]
sb.set(rc={"figure.figsize":(13, 5)}) #width=6, height=5
fig = sb.boxplot(df,x='relativeYcenterBBox',y='dataset').get_figure()
fig.tight_layout()
#plt.xlim(0, 1100)
#sb.set(rc={"figure.figsize":(13, 4)}) #width=3, #height=4
fig.savefig(outputImgFolder+'boxplot_'+feature+'.png', dpi=200)

plt.cla()
plt.clf()
plt.close()

df['relativeXcenterBBox'] = df['XcenterBBox'] / df['Xax']

feature = 'relativeXcenterBBox'
#dataset = path.split('/')[-1]
#data = df[df['dataset']==dataset]
sb.set(rc={"figure.figsize":(13, 5)}) #width=6, height=5
fig = sb.boxplot(df,x='relativeXcenterBBox',y='dataset').get_figure()
fig.tight_layout()
#plt.xlim(0, 1100)
#sb.set(rc={"figure.figsize":(13, 4)}) #width=3, #height=4
fig.savefig(outputImgFolder+'boxplot_'+feature+'.png', dpi=200)



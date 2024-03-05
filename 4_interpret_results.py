import os
import pandas as pd
import matplotlib.pyplot as plt
import scipy
plt.style.use('seaborn')

exportFolder = '/home/jean-pierre/ownCloud/phd/experiments_2023'

files = [
    '/home/jean-pierre/ownCloud/phd/experiments_2023/resultsAll_20201117_3SamsungGalaxyA5.ods',
    '/home/jean-pierre/ownCloud/phd/experiments_2023/resultsAll_20201119_3pi4.ods',
    '/home/jean-pierre/ownCloud/phd/experiments_2023/resultsAll_20201126_4pi4_c5.ods',
    '/home/jean-pierre/ownCloud/phd/experiments_2023/resultsAll_20201303_1pi4_sampled.ods',
    '/home/jean-pierre/ownCloud/phd/experiments_2023/resultsAll_2022_randomWoodImages.ods',
    '/home/jean-pierre/ownCloud/phd/experiments_2023/resultsAll_20191125_Allier1.ods'
]




for file in files:
    print(' ')
    outputFile = os.path.join(exportFolder,(file.split('/')[-1]).split('.')[0]+'.png')
    print(outputFile)
    df = pd.read_excel(file)
    #plt.figure(figsize=(8, 12), dpi=160)
    df.plot.box(patch_artist=True)
    plt.title(((file.split('/')[-1]).split('.')[0]).split('resultsAll_')[1])
    plt.xlabel('Scenario')
    plt.ylabel('mean Average Precision (mAP)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(outputFile, dpi=400)

    columnlist = df.columns.tolist()

    for item in columnlist:
        if item != 'jpgs':
            kruskal = scipy.stats.kruskal(df["jpgs"],df[item])
            if kruskal.pvalue < 0.05:
                print('DIFFERENT '+str(item)+':')
            print(kruskal)


df1 = pd.read_excel('/home/jean-pierre/ownCloud/phd/experiments_2023/resultsAll_20201117_3SamsungGalaxyA5.ods')
df2 = pd.read_excel('/home/jean-pierre/ownCloud/phd/experiments_2023/resultsAll_20201119_3pi4.ods')
df3 = pd.read_excel('/home/jean-pierre/ownCloud/phd/experiments_2023/resultsAll_20201126_4pi4_c5.ods')
df4 = pd.read_excel('/home/jean-pierre/ownCloud/phd/experiments_2023/resultsAll_20201303_1pi4_sampled.ods')
df5 = pd.read_excel('/home/jean-pierre/ownCloud/phd/experiments_2023/resultsAll_2022_randomWoodImages.ods')
df6 = pd.read_excel('/home/jean-pierre/ownCloud/phd/experiments_2023/resultsAll_20191125_Allier1.ods')

#dfall = pd.concat(df2)
#print(dfall)
dfall = pd.concat([df1,df2,df3,df4,df5,df6])



'''
count = 0
for file in files:
    df = pd.read_excel(file)
    print(df)
    if count != 0:
        dfall = pd.merge(df,dfmem)
    dfmem = df
    count = count + 1
'''
#print(dfall)



outputFile = os.path.join(exportFolder,'resultsAllCombined.png')
print(outputFile)
#plt.figure(figsize=(8, 12), dpi=160)
dfall.plot.box(patch_artist=True)
plt.title('resultsAllCombined')
plt.xlabel('Scenario')
plt.ylabel('mean Average Precision (mAP)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig(outputFile, dpi=400)



columnlist = dfall.columns.tolist()

for item in columnlist:
    if item != 'jpgs':
        kruskal = scipy.stats.kruskal(dfall["jpgs"],dfall[item])
        if kruskal.pvalue < 0.05:
            print('DIFFERENT:')
        print(kruskal)
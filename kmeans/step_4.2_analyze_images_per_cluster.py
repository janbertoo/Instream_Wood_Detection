import numpy as np
import pandas as pd
from scipy import stats

#define the numpy file to load
file = '/home/jean-pierre/ownCloud/phd/code_code_code_code_code/1MAIN_processing/KMEANS/allWoods200_normalized_centered/pictureNamesAndClusters_clus_nums_20silhouette_0.032318450025151206.npy'



amount_of_classes = int((file.split('nums_')[1]).split('silhouette')[0])
print(amount_of_classes)

datasets = [
    '20201117_rotated__1pi2',
    '20201117_rotated__2pi4',
    '20201117_rotated__3SamsungGalaxyA5',
    '20201117_rotated__4XiaomiRedmi4X',
    '20201119_rotated__1XiaomiRedmi4X',
    '20201119_rotated__2pi2',
    '20201119_rotated__3pi4',
    '20201119_rotated__4SamsungGalaxyA5_sampled',
    '20201126_rotated__3XiaomiRedmi2_sampled',
    '20201126_rotated__4pi4_c4_sampled',
    '20201126_rotated__4pi4_c5',
    '20201127_rotated__2pi4',
    '20201203_rotated__1pi4_sampled',
    '20201203_rotated__3pi2',
    '20201203_rotated__4SamsungGalaxyA5',
    'unilyon_and_others__20071123_0756_Ain1',
    'unilyon_and_others__20071123_0956_Ain2',
    'unilyon_and_others__20191125_Allier1',
    'unilyon_and_others__20191223_Allier2',
    'unilyon_and_others__randomWoodImages'
]

clusters = [
    '20201117',
    '20201119',
    '20201126',
    '20201203',
    'Ain',
    'Allier'
]

captureclusters = [
    'pi',
    'SamsungGalaxyA5',
    'XiaomiRedmi4X'
]

data = np.load(file)
print(data)
datasetsWithAmount = []

df = pd.DataFrame(data)
print(df)

for cluster in clusters:
    dataframe1 = df[df[0].str.contains(cluster)]
    print("")
    
    for dataset in datasets:
        
        dataframe2 = df[df[0].str.contains(dataset)]
        
        
        merged = pd.merge(
            dataframe1[1].value_counts().to_frame(),
            dataframe2[1].value_counts().to_frame(),
            left_index=True,
            right_index=True)
        #print(cluster+" + "+dataset+", amount of images in cluster and dataset: "+str(len(dataframe1))+", "+str(len(dataframe2)))
        #print(stats.ks_2samp(merged.count_x, merged.count_y).statistic)
        #print(stats.ks_2samp(merged.count_x, merged.count_y).pvalue)
        #print(stats.ks_2samp(merged.count_x, merged.count_y).pvalue)
        print(stats.ks_2samp(merged.count_x, merged.count_y).pvalue)
        #if stats.ks_2samp(merged.count_x, merged.count_y).pvalue < 0.05:
        #    print(cluster+" + "+dataset+", amount of images in cluster and dataset: "+str(len(dataframe1))+", "+str(len(dataframe2)))
        #    print(stats.ks_2samp(merged.count_x, merged.count_y).statistic)
        #    print(stats.ks_2samp(merged.count_x, merged.count_y).pvalue)




'''
#count the amount of examples per dataset
for dataset in datasets:
    count = 0
    for image in data:
        if dataset in image[0]:
            count = count + 1
    percentage = (count / len(data) ) * 100
    datasetsWithAmount.append([dataset,count,percentage])

print(datasetsWithAmount)



countPercentage = 0
for percentage in datasetsWithAmount:
    countPercentage = countPercentage + percentage[2]

if countPercentage != 100:
    print('total percentage is not 100, something is wrong')
    print('Percentage is: '+str(countPercentage))

datawithdatasetassigned = []

for i in range(len(data)):
    for dataset in datasets:
        datasetNameLength = len(dataset)
        if data[i][0][:datasetNameLength] == dataset:
            clusterName = None
            for cluster in clusters:
                clusterLength = len(cluster)
                #if data[i][0][:clusterLength] == cluster or data[i][0][-clusterLength:] == cluster:
                if cluster in data[i][0]:
                    clusterName = cluster
            captureClusterName = None
            for capturecluster in captureclusters:
                captureclusterLength = len(capturecluster)
                if capturecluster in data[i][0]:
                    captureClusterName = capturecluster
            datawithdatasetassigned.append((data[i][0],data[i][1],dataset,clusterName,captureClusterName))

df = pd.DataFrame (datawithdatasetassigned, columns = ['img_name','class_number','dataset','date_cluster','capture_cluster'])

print(df)
print(' ')
print(df.info())
print(' ')
#print(df.skew())
print(' ')
print(df.describe())

crosstab1 = pd.crosstab(index=df['class_number'],columns=df['date_cluster'])
crosstab2 = pd.crosstab(index=df['class_number'],columns=df['capture_cluster'])

print(' ')
print(crosstab1.skew())
print(' ')
print(crosstab2.skew())
print(' ')

print(' ')
print(df)

groupedpercluster = df.groupby('class_number')#[['date_cluster','capture_cluster']]

for i in range(amount_of_classes):
    print('')
    print('class '+str(i))
    groupedClusterNumber = (groupedpercluster.get_group(str(i))).groupby('date_cluster')
    #print(groupedClusterNumber)
    amountOfImangesInThisCluster = len(groupedpercluster.get_group(str(i)))
    for datecluster in clusters:
        amountOfImagesInCluster = len(groupedClusterNumber.get_group(datecluster))
        percentageOfImagesInCluster = (amountOfImagesInCluster / amountOfImangesInThisCluster ) * 100        
        print(datecluster+': '+str(len(groupedClusterNumber.get_group(datecluster)))+', percentage: '+str(percentageOfImagesInCluster))
    print('')
    groupedClusterNumber = (groupedpercluster.get_group(str(i))).groupby('dataset')
    #print(groupedClusterNumber)
    amountOfImangesInThisDataset = len(groupedpercluster.get_group(str(i)))
    #print('IMAGE IN THIS DATASET: ')
    #print(amountOfImangesInThisDataset)
    for dataset in datasets:
        try:
            amountOfImagesInDataset = len(groupedClusterNumber.get_group(dataset))
            percentageOfImagesInDataset = (amountOfImagesInDataset / amountOfImangesInThisDataset ) * 100        
            print(dataset+': '+str(len(groupedClusterNumber.get_group(dataset)))+', percentage: '+str(percentageOfImagesInDataset))
        except:
            print(dataset+': 0, percentage: 0')



print(' ')

clustersPlusPercentage = []

for cluster in clusters:
    totPercentage = 0
    for datasetWithAmount in datasetsWithAmount:
        if cluster in datasetWithAmount[0]:
            #print(datasetWithAmount)
            totPercentage = totPercentage + datasetWithAmount[2]
    clustersPlusPercentage.append((cluster,totPercentage))
print('total percentages:')
[print(clusterPercentage) for clusterPercentage in clustersPlusPercentage]
print('')
print('now per cluster:')
for cluster in clusters:
    data = df[df['date_cluster']==cluster]
    #print(data)
    countDFlist = []
    totalAmountOfImsInCluster = 0
    for i in range(amount_of_classes):
        #total = data['class_number'].value_counts()[i]
        try:
            total = data[data['class_number'] == str(i)].count()[0]
        except:
            total = 0
        totalAmountOfImsInCluster = totalAmountOfImsInCluster + total
        countDFlist.append(
            {
                'cluster' : cluster,
                'class_no': i,
                'count' : total
                                }
        )
    print(count)
    dfcount = pd.DataFrame(countDFlist)
    dfcount['percentage'] = ( dfcount['count'] / totalAmountOfImsInCluster ) * 100
    print(dfcount)

dataframe1 = dfcount


print("")
print("now per dataset:")
for dataset in datasets:
    print('')
    print('')
    data = df[df['dataset']==dataset]
    #print(data)
    #print('value counts:')
    #valueCounts = data['class_number'].value_counts().sort_index()
    #print(valueCounts)

    countDFlist = []
    totalAmountOfImsInCluster = 0
    for i in range(amount_of_classes):
        #print('CLASS: '+str(i))
        try:
            #total = data['class_number'].value_counts()[i]
            try:
                #total = valueCounts[i]
                total = data[data['class_number'] == str(i)].count()[0]
            except:
                total = 0
            #print(total)
            totalAmountOfImsInCluster = totalAmountOfImsInCluster + total
            countDFlist.append(
                {
                    'dataset' : dataset,
                    'class_no': i,
                    'count' : total
                                    }
            )
        except:
            print('No samples in cluster '+str(i))
        #print('Tot ims: '+str(count))
        dfcount = pd.DataFrame(countDFlist)
        dfcount['percentage'] = ( dfcount['count'] / totalAmountOfImsInCluster ) * 100
    print(dfcount)
    #print('')

dataframe2 = dfcount


print(dataframe1)
print(dataframe2)
'''

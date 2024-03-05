import os

paths = [
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
    '/home/jean-pierre/scratch/unilyon_and_others/20191223_Allier2/labeled_20191223_Allier2',
    '/home/jean-pierre/scratch/unilyon_and_others/randomWoodImages/labeled_2022_randomWoodImages'
]

#samplesPerDataset = [1429,601,1076,478,344,2478,2146,191,18,138,1046,1034,157,2340,1236,116,81,176,134,9]
#print(samplesPerDataset)
originalToCount = 'jpgs'
samplesPerDataset = []

#get a list of the amount of samples per dataset
for path in paths:
    jpgsFolder = os.path.join(path,originalToCount)
    files = os.listdir(jpgsFolder)
    samplesPerDataset.append(len(files))
'''
trimmedV2ToCount = 'jpgs_trimmedV2'
samplesPerDatasetTrimmedV2 = []

#get a list of the amount of samples per dataset
for path in paths:
    jpgsFolder = os.path.join(path,trimmedV2ToCount)
    files = os.listdir(jpgsFolder)
    samplesPerDatasetTrimmedV2.append(len(files))
'''
total = 0
for number in samplesPerDataset:
    total = total + number

print(total)

samplesPerDatasetHybrid = [750,601,750,478,344,750,750,250,250,250,750,750,250,750,750,250,250,250,250,250]

total = 0
for number in samplesPerDatasetHybrid:
    total = total + number

print(total)

samplesPerDatasetHybrid2 = [1000,601,1000,500,500,1000,1000,500,500,500,1000,1000,500,100,1000,500,500,500,500,500]

total = 0
for number in samplesPerDatasetHybrid2:
    total = total + number

print(total)

samplesPerDatasetHybrid3 = [1429,601,1076,500,500,1500,1500,500,500,500,1046,1034,500,1500,1236,500,500,500,500,500]

total = 0
for number in samplesPerDatasetHybrid3:
    total = total + number

print(total)

samplesPerDatasetHybrid4 = [1200,601,1076,500,500,1200,1200,500,500,500,1046,1034,500,1200,1200,500,500,500,500,500]

total = 0
for number in samplesPerDatasetHybrid4:
    total = total + number

print(total)
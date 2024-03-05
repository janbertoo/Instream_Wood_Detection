import os, shutil

jpgsFolder = 'jpgs'
txtsFolder = 'txts'

paths = [
	'/home/jean-pierre/scratch/internetVideos/canada_del_oro/labeled_2022_canada_del_oro',
	'/home/jean-pierre/scratch/internetVideos/hikuwai_river_NZ/labeled_2023_hikuwai_river_NZ',
	'/home/jean-pierre/scratch/internetVideos/ilfis_river/labeled_2022_ilfis_river',
	'/home/jean-pierre/scratch/internetVideos/north_creek/labeled_20180802_north_creek',
	'/home/jean-pierre/scratch/internetVideos/north_creek_2_plus_trabuco_creek/labeled_2022_north_creek_2_plus_trabuco_creek',
	'/home/jean-pierre/scratch/internetVideos/north_creek_3/labeled_2022_north_creek_3',
	'/home/jean-pierre/scratch/internetVideos/piha_valley_Auckland/labeled_piha_valley_Auckland',
	'/home/jean-pierre/scratch/internetVideos/rio_moquegua/labeled_20190205_rio_moquegua',
	'/home/jean-pierre/scratch/internetVideos/sihl_a_studen/labeled_2022_sihl_a_studen',
	'/home/jean-pierre/scratch/extra_own_data/20220520_rhone_data/labeled_20220520_rhone_data',
	'/home/jean-pierre/scratch/extra_own_data/VDN_vid_20210509_174821/labeled_VDN_vid_20210509_174821',
	'/home/jean-pierre/scratch/extra_own_data/VDN_vid_20210509_180320/labeled_VDN_vid_20210509_180320'
	]
'''
paths = [
    '/home/jean-pierre/Desktop/VDN_vid_20210509_174821/labeled_VDN_vid_20210509_174821'
]
'''
for path in paths:
    prestention = ((path.split('/')[-1]).split('labeled_')[-1])+'_'

    jpgsPath = os.path.join(path,jpgsFolder)
    txtsPath = os.path.join(path,txtsFolder)

    for jpg in os.listdir(jpgsPath):
        shutil.move(os.path.join(jpgsPath,jpg),os.path.join(jpgsPath,prestention+jpg))
        shutil.move(os.path.join(txtsPath,jpg.replace('.jpg','.txt')),os.path.join(txtsPath,(prestention+jpg).replace('.jpg','.txt')))
import os
import shutil

jpgsFolder = 'jpgs'

txtsFolder = jpgsFolder.replace('jpgs','txts')
allFolder = jpgsFolder.replace('jpgs', 'all')

folderToCopyToAll = os.path.join('/home/jean-pierre/scratch/',allFolder)

print(' ')
print('making dir: '+folderToCopyToAll)
print(' ')


try:
    os.mkdir(folderToCopyToAll)
except:
    shutil.rmtree(folderToCopyToAll)
    os.mkdir(folderToCopyToAll)

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

for path in paths:
    print(path)
    for jpgfile in os.listdir(os.path.join(path,jpgsFolder)):
        if jpgfile[-4:] == '.jpg':
            orFileJpg = os.path.join(path,jpgsFolder,jpgfile)
            shutil.copy(orFileJpg, folderToCopyToAll)
            #print('copying '+orFileJpg+' to '+folderToCopyToAll)

for path in paths:
    for txtfile in os.listdir(os.path.join(path,txtsFolder)):
        if txtfile[-4:] == '.txt':
            orFileTxt = os.path.join(path,txtsFolder,txtfile)
            shutil.copy(orFileTxt, folderToCopyToAll)
            #print('copying '+orFileTxt+' to '+folderToCopyToAll)

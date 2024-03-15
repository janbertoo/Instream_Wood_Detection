import os
import shutil

jpgsFolder = 'jpgs_only_rotate_random_V2'
newJpgsFolder = 'jpgs_only_rotate_random_V3'


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
]

for path in paths:
    print(path)
    shutil.move(os.path.join(path,jpgsFolder),os.path.join(path,newJpgsFolder))
    shutil.move(os.path.join(path,jpgsFolder.replace('jpgs','txts')),os.path.join(path,newJpgsFolder.replace('jpgs','txts')))

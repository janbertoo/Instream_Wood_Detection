import os

configFile = os.path.join(os.getcwd(),'yolov4_custom.cfg')

folder = 'jpgs'

addon = 'double_res'

database_base_path = '/home/jean-pierre/scratch-double_res/'

orPaths = [
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
    database_base_path+'unilyon_and_others/randomWoodImages/labeled_2022_randomWoodImages',
#	database_base_path+'internetVideos/canada_del_oro/labeled_2022_canada_del_oro',
#	database_base_path+'internetVideos/ilfis_river/labeled_2022_ilfis_river',
#	database_base_path+'internetVideos/north_creek/labeled_20180802_north_creek',
#	database_base_path+'north_creek_2_plus_trabuco_creek/labeled_2022_north_creek_2_plus_trabuco_creek',
#	database_base_path+'north_creek_3/labeled_2022_north_creek_3',
#	database_base_path+'rio_moquegua/labeled_20190205_rio_moquegua',
#	database_base_path+'sihl_a_studen/labeled_2022_sihl_a_studen',
#	database_base_path+'extra_own_data/20220520_rhone_data/labeled_20220520_rhone_data',
#	database_base_path+'extra_own_data/VDN_vid_20210509_174821/labeled_VDN_vid_20210509_174821',
#	database_base_path+'extra_own_data/VDN_vid_20210509_180320/labeled_VDN_vid_20210509_180320',
]

paths = []

for path in orPaths:
	paths.append(os.path.join(path,folder))

pathToWrite = 'data/obj/'
#pathToWriteTrain = 'data/objTrain/'
#pathToWriteValidate = 'data/objValidate/'

def createTrainingTxt(testPath, allPaths):
	txtName = "train_minus_"+(testPath.split('/')[-2]).split('beled_')[1]+addon+'.txt'
	validName = "validate_"+(testPath.split('/')[-2]).split('beled_')[1]+addon+'.txt'
	configName = "config_yolov4_custom_"+(testPath.split('/')[-2]).split('beled_')[1]+addon+'.cfg'

	os.system('cp '+configFile+' '+configName)

	with open(txtName, 'w') as f:
		for path in allPaths:
			if path == testPath:
				continue
			else:
				for jpg in os.listdir(path):
					f.write(pathToWrite+jpg+'\n')

	with open(validName, 'w') as g:
		for path in allPaths:
			pathReplaced = path.replace(folder,'jpgs')
			if path == testPath:
				for jpg in os.listdir(pathReplaced):
					g.write(pathToWrite+jpg+'\n')
			else:
				continue

	objDataName = "obj_train_minus_"+(testPath.split('/')[-2]).split('beled_')[1]+addon+'.data'
	minus = "minus_"+(testPath.split('/')[-2]).split('beled_')[1]
	with open(objDataName, 'w') as d:
		d.write('classes = 1\n')
		d.write('train = data/'+txtName+'\n')
		d.write('valid = data/'+validName+'\n')
		d.write('names = data/obj.names\n')
		d.write('backup = ../training\n')

	return objDataName, configName, minus


count = 1
for path in paths:
	objDataName, configName, minus = createTrainingTxt(path, paths)
	print(objDataName)
	#create sbatch script
	with open('runJobsGPU'+addon+'_'+str(count)+'_'+minus+'.sh','w') as e:
		e.write('#!/bin/bash\n')
		e.write('\n')
		e.write('#SBATCH --nodes 1\n')
		e.write('#SBATCH --ntasks 1\n')
		e.write('#SBATCH --cpus-per-task 6\n')
		e.write('#SBATCH --mem 12G\n')
		e.write('#SBATCH --time 12:00:00\n')
		e.write('#SBATCH --account vruizvil_rives\n')
		e.write('\n')
		e.write('# change directory to the directory on the scratch where the data is located\n')
		e.write('\n')
		e.write('#SBATCH --chdir /scratch/jaarnink/yoloV4/darknet\n')
		e.write('#SBATCH --output /scratch/jaarnink/yoloV4/darknet_job_'+addon+'_'+str(count)+'_'+minus+'.out\n')
		e.write('\n')
		e.write('# NOTE - GPUS are in the gpu partition\n')
		e.write('\n')
		e.write('#SBATCH --partition gpu\n')
		e.write('#SBATCH --gres gpu:1\n')
		e.write('#SBATCH --gres-flags enforce-binding\n')
		e.write('\n')
		e.write('# Set up my modules\n')
		e.write('\n')
		e.write('module purge\n')
		e.write('module load gcc python cuda cudnn opencv\n')
		e.write('\n')
		e.write('# Check that the GPU is visible\n')
		e.write('\n')
		e.write('nvidia-smi\n')
		e.write('\n')
		e.write('# Run my GPU enable python code\n')
		e.write('\n')
		e.write('/work/FAC/FGSE/IDYST/vruizvil/rives/darknet/darknet detector train /scratch/jaarnink/yoloV4/darknet/data/'+objDataName+' /scratch/jaarnink/yoloV4/darknet/cfg/'+configName+' /scratch/jaarnink/yoloV4/training/yolov4.conv.137 -dont_show -map\n')

	count = count + 1

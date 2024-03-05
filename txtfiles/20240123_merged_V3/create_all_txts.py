import os

configFile = os.path.join(os.getcwd(),'yolov4_custom.cfg')

folder = 'jpgs_merged'

addon = '_20240123_jpgs_merged_V3'


orPaths = [
	'/home/jean-pierre/ownCloud/phd/labeled_data_all/20201117_rotated/1pi2/labeled_20201117_1pi2_c3',
	'/home/jean-pierre/ownCloud/phd/labeled_data_all/20201117_rotated/2pi4/labeled_20201117_2pi4_c1',
	'/home/jean-pierre/ownCloud/phd/labeled_data_all/20201117_rotated/3SamsungGalaxyA5/labeled_20201117_3SamsungGalaxyA4_OC',
	'/home/jean-pierre/ownCloud/phd/labeled_data_all/20201117_rotated/4XiaomiRedmi4X/labeled_20201117_4XiaomiRedmi4X_OC',
	'/home/jean-pierre/ownCloud/phd/labeled_data_all/20201119_rotated/1XiaomiRedmi4X/labeled_20201119_1XiaomiRedmi4X_OC',
	'/home/jean-pierre/ownCloud/phd/labeled_data_all/20201119_rotated/2pi2/labeled_20201119_2pi2_c3',
	'/home/jean-pierre/ownCloud/phd/labeled_data_all/20201119_rotated/3pi4/labeled_20201119_3pi4_c3',
	'/home/jean-pierre/ownCloud/phd/labeled_data_all/20201119_rotated/4SamsungGalaxyA5_sampled/labeled_20201119_4SamsungGalaxyA_OC_sampled',
	'/home/jean-pierre/ownCloud/phd/labeled_data_all/20201126_rotated/3XiaomiRedmi2_sampled/labeled_20201126_3XiaomiRedmi2_OC2_sampled',
	'/home/jean-pierre/ownCloud/phd/labeled_data_all/20201126_rotated/4pi4_c4_sampled/labeled_20201126_4pi4_c4_sampled',
	'/home/jean-pierre/ownCloud/phd/labeled_data_all/20201126_rotated/4pi4_c5/labeled_20201126_4pi4_c5',
	'/home/jean-pierre/ownCloud/phd/labeled_data_all/20201127_rotated/2pi4/labeled_20201127_2pi4_c2',
	'/home/jean-pierre/ownCloud/phd/labeled_data_all/20201203_rotated/1pi4_sampled/labeled_20201203_1pi4_c20_sampled',
	'/home/jean-pierre/ownCloud/phd/labeled_data_all/20201203_rotated/3pi2/labeled_20201203_3pi2_c4',
	'/home/jean-pierre/ownCloud/phd/labeled_data_all/20201203_rotated/4SamsungGalaxyA5/labeled_20201203_4SamsungGalaxyA5_OC',
	'/home/jean-pierre/ownCloud/phd/labeled_data_all/unilyon_and_others/20071123_0756_Ain1/labeled_20071123_0756_Ain1',
	'/home/jean-pierre/ownCloud/phd/labeled_data_all/unilyon_and_others/20071123_0956_Ain2/labeled_20071123_0956_Ain2',
	'/home/jean-pierre/ownCloud/phd/labeled_data_all/unilyon_and_others/20191125_Allier1/labeled_20191125_Allier1',
	'/home/jean-pierre/ownCloud/phd/labeled_data_all/unilyon_and_others/20191223_Allier2/labeled_20191223_Allier2',
#	'/home/jean-pierre/ownCloud/phd/labeled_data_all/unilyon_and_others/randomWoodImages/labeled_2022_randomWoodImages',
#	'/home/jean-pierre/ownCloud/phd/labeled_data_all/internetVideos/canada_del_oro/labeled_2022_canada_del_oro',
#	'/home/jean-pierre/ownCloud/phd/labeled_data_all/internetVideos/ilfis_river/labeled_2022_ilfis_river',
#	'/home/jean-pierre/ownCloud/phd/labeled_data_all/internetVideos/north_creek/labeled_20180802_north_creek',
#	'/home/jean-pierre/ownCloud/phd/labeled_data_all/internetVideos/north_creek_2_plus_trabuco_creek/labeled_2022_north_creek_2_plus_trabuco_creek',
#	'/home/jean-pierre/ownCloud/phd/labeled_data_all/internetVideos/north_creek_3/labeled_2022_north_creek_3',
#	'/home/jean-pierre/ownCloud/phd/labeled_data_all/internetVideos/rio_moquegua/labeled_20190205_rio_moquegua',
#	'/home/jean-pierre/ownCloud/phd/labeled_data_all/internetVideos/sihl_a_studen/labeled_2022_sihl_a_studen'
#	'/home/jean-pierre/ownCloud/phd/labeled_data_all/extra_own_data/dry_wood_data_VDN_2021',
#	'/home/jean-pierre/ownCloud/phd/labeled_data_all/extra_own_data/dry_wood_data_VDN_2022',
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
			pathReplaced = path.replace(folder,'jpgs_merged')
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
		e.write('#SBATCH --chdir /work/FAC/FGSE/IDYST/vruizvil/rives/darknet_data\n')
		e.write('#SBATCH --output /work/FAC/FGSE/IDYST/vruizvil/rives/darknet_data/darknet_job_'+addon+'_'+str(count)+'_'+minus+'.out\n')
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
		e.write('/work/FAC/FGSE/IDYST/vruizvil/rives/darknet/darknet detector train /work/FAC/FGSE/IDYST/vruizvil/rives/darknet_data/data/'+objDataName+' /work/FAC/FGSE/IDYST/vruizvil/rives/darknet_data/cfg/'+configName+' /work/FAC/FGSE/IDYST/vruizvil/rives/darknet_data/yolov4.conv.137 -dont_show -map\n')

	count = count + 1

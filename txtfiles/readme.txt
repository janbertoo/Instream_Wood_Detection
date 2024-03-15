To perform the experiments, first a working version of darknet needs to be installed.
Also the database needs to be present.

For each scenario, the data can be created using the scripts in the main folder. Make sure that all the augmented/merged/sampled data is correctly in the 'database_base_path' folder. The following script will go throught the folder and create the necessary documents you need to run the YoloV4 training.

1. Create a folder with the experiment name
2. Adjust the sample config file for YOLOv4 to the folder to represent your experiment (changes when doubling the resolution)
3. In the 'create_all_txts.py' python file, add the locations of the datasets that will form either the training of the validation dataset.
4. Run the python script to create all the needed files for the YOLOv4 training process

These files can be copied to a cluster.
Copy all the '.txt' and '.data' files to the local 'darknet/data/' folder.
Copy all the '.cfg' files to the local 'darknet/cfg/' folder.

Also make sure that the .jpg files and the .txt files are present in the correct folder. The correct folder can be found in the followin txt files (generally the data/obj/ folder in darknet).
"train_minus_DATASET-NAME.txt'
"validate_DATASET-NAME.txt'

The 'runJob*.sh' scripts can be ran to perform an experiment using sbatch on a cluster where darknet is installed.

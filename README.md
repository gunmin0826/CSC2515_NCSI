# CSC2515_NCSI
neural cloth simulation (but improved)


## Download the animation files (.fbx) from Mixamo
Use downloadAll.js script and link provided in references.txt 


## turn .fbx files into .npz files
From NeuralClothSim/mixamo_processing/ directory run 'run_get_sequence.sh' bash script to process all the .fbx files in NeuralClothSim/motions/ to .npz files in NeuralClothSim/data/mixamo/

The bash script will change all the space characters inside the .fbx filenames to under score ('file name.fbx' ==> 'file_name.fbx') to easily iterate through  file names.



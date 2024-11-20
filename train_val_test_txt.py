### This file searches through the name of .npz file in NeuralClothSim/data/mixamo directory
### creates three text files train.txt val.txt and test.txt in NeuralClothSim/ncs/dataset/txt/mixamo/
### the .npz files written in each text file will be used for corressponding part of the program

import os
import sys
import math
import random

def main(src, dst):

    TRAIN = 0.7
    VAL = 0.15
    TEST = 0.15

    if TRAIN+VAL+TEST > 1:
        print("TRAIN+VAL+TEST > 1")
        return

    print(f"src: {src}")
    print(f"dst: {dst}")
    # return 
    assert os.path.isdir(src), f"Folder does not exist: {src}"
    assert os.path.isdir(dst), f"Folder does not exist: {dst}"
    files = os.listdir(src)
    npz_files = []
    for file in files:
        if file[-4:] == '.npz':
            npz_files.append(file)
    
    # print(f"npz_files:\n{npz_files}")
    num_files = len(npz_files)
    num_train = math.floor(num_files*TRAIN)
    num_val = math.floor(num_files*VAL)
    num_test = num_files - (num_train + num_val)
    if num_train + num_val + num_test != num_files:
        print(f"num_train + num_val + num_test != num_files")
        return
    
    train_data = [npz_files.pop(random.randrange(len(npz_files))) for _ in range(num_train)]
    val_data = [npz_files.pop(random.randrange(len(npz_files))) for _ in range(num_val)]
    test_data = npz_files  
    
    # print(f"\ntrain_data:\n{train_data}")
    # print(f"\nval_data:\n{val_data}")
    # print(f"\ntest_data:\n{test_data}")

    train_string = '\n'.join(train_data)
    val_string = '\n'.join(val_data)
    test_string = '\n'.join(test_data)
    # print(f"train_string:\n{train_string}")
    # write file names to text file

    f = open(dst + "/train.txt", "w")
    f.write(train_string)
    f.close()

    f = open(dst + "/val.txt", "w")
    f.write(val_string)
    f.close() 

    f = open(dst + "/test.txt", "w")
    f.write(test_string)
    f.close()
    


if __name__ == '__main__':
    main(src=sys.argv[1], dst=sys.argv[2])
    
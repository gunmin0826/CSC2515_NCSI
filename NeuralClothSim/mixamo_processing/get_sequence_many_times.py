import os 
import sys


def main(src, dst):
    print(f"origin:{src}")
    print(f"dst:{dst}")

    current_dir = os.getcwd() # <-- use these lines in blender script
    # print("current_dir")
    dir = current_dir+'/'+src
    print(f"dir:{dir}")
    dest = current_dir+'/'+dst
    print(f"dest:{dest}")

    assert os.path.isdir( 
        os.path.dirname(dir)
    ), f"Directory does not exist: {os.path.dirname(dir)}"
    assert os.path.isdir(
        os.path.dirname(dest)
    ), f"Folder does not exist: {os.path.dirname(dest)}"

    # find list of source .fbx files 
    source_files = os.listdir(dir)
    source_files.sort()
    # print(f"source_files: {source_files}")
    
    for src_file in source_files:
        name = src_file.split('/')[-1]
        name = name[:-4] # get rid of .fbx characters
        print(f"name:{name}")
        file_path = src + "/" + src_file
        dst_path = dst + "/" + name + '.npz'
        print(f"file_name: {file_path}")
        print(f"dst_path: {dst_path}")
        print()
        os.system("python get_sequence.py " + '"' + file_path + '"' + " " + '"' + dst_path + '"')
        # print("blender --python get_sequence.py " + '"' + file_path + '"' + " " + '"' + dst_path + '"')
        break

if __name__ == "__main__":
    main(src=sys.argv[1], dst=sys.argv[2]) # richard's
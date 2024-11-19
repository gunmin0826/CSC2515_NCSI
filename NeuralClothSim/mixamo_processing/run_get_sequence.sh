#!/bin/bash

# Path to your Python script
PYTHON_SCRIPT="get_sequence.py"

# Source directory containing .fbx files
SOURCE_DIR="../motions"

# Output directory for processed files
OUTPUT_DIR="../data/mixamo"

# replace all spaces in filenames to underscores
find $SOURCE_DIR -type f -name "* *" | while read file; do mv "$file" ${file// /_}; done

# Find all .fbx files in the source directory
FBX_FILES=$(find "$SOURCE_DIR" -type f -name "*.fbx")


# Loop through the .fbx files
for fbx_file in $FBX_FILES
do
    # Get the filename without path and extension
    filename=$(basename "$fbx_file" .fbx)
    
    # Construct the output path
    output_path="$OUTPUT_DIR/${filename}.npz"

    # Run Blender command
    blender --python "$PYTHON_SCRIPT" "$fbx_file" "$output_path"
done

# ls
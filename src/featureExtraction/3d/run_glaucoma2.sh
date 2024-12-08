#!/bin/bash

SCRIPT="python3 glaucoma/glaucoma.py"
CONFIG_FILE="--config-file configs/pix3d/meshrcnn_R50_FPN.yaml"
INPUT_PATH="GlaucomaDataset485SubjectsImages/retinographies/glaucoma/glaucoma"
OUTPUT_DIR="--output output_glaucoma"
WEIGHTS="--onlyhighest MODEL.WEIGHTS meshrcnn://meshrcnn_R50.pth"

for i in {169..172}; do
  IMAGE_NUM=$(printf "%03d" $i)
  INPUT_IMAGE="${INPUT_PATH}${IMAGE_NUM}.png"
  
  # Make the mesh inference
  $SCRIPT $CONFIG_FILE --input $INPUT_IMAGE $OUTPUT_DIR $WEIGHTS
  
  sleep 3
done
#!/bin/bash
ENV='C:/Users/Seeking/Anaconda3/envs/pyqt6'
pyuic=${ENV}'/Scripts/pyuic6'

ROOT=''
INPUT_DIR='export-ui/ui_design/ui'
OUTPUT_DIR='export-ui/ui_design/py'
FILE_NAME='ui_onnx2engine'

output=${ROOT}/${INPUT_DIR}/${FILE_NAME}'.py'
input=${ROOT}/${OUTPUT_DIR}/${FILE_NAME}'.ui'

${pyuic} -o ${output} ${input}

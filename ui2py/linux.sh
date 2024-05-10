#!/bin/bash
pyuic='C:\Users\Seeking\Anaconda3\envs\pyqt6\Scripts\pyuic6'
output='D:\llf\code\export-ui\ui\onnx2engine.py'
input='D:\llf\code\export-ui\ui\onnx2engine.ui'
${pyuic} -o ${output} ${input}

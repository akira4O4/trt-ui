SET env=C:\Users\Seeking\Anaconda3\envs\pyqt5
SET pyuic=%env%\Scripts\pyuic5
SET root=D:\llf\code\export-ui\ui\ui_onnx2engine
SET input=%root%.ui
SET output=%root%.py

%pyuic% -o %output% %input%

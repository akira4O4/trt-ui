SET ENV=C:\Users\Seeking\Anaconda3\envs\pyqt5
SET pyuic=%ENV%\Scripts\pyuic5

SET ROOT=D:\llf\code
SET INPUT_DIR=export-ui\ui_design\ui
SET OUTPUT_DIR=export-ui\ui_design\py
SET FILE_NAME=ui_onnx2engine

SET input=%ROOT%\%INPUT_DIR%\%FILE_NAME%.ui
SET output=%ROOT%\%OUTPUT_DIR%\%ufile_name%.py

%pyuic% -o %output% %input%

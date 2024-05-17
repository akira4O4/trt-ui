import os
import time

from loguru import logger

from PyQt5.QtCore import QUrl
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QDesktopServices, QColor, QPalette
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox

from src.deonnx import DeONNX
from src.colors import Colors
from src.filepath import FilePath
from src.configfile import ConfigFile
from src.utils import list2str, str2list
from src.impl.convert_progressbar import ConvertProgressBar
from .export_thread import ExportThread
from views.py.ui_onnx2engine import Ui_ONNX2Engine


class ONNX2Engine(QMainWindow, Ui_ONNX2Engine):

    def __init__(self, config_path: str) -> None:

        super().__init__()
        self.colors = Colors
        self.config = ConfigFile(config_path)
        self.export_thread = ExportThread()
        self.convert_progressbar = ConvertProgressBar()

        # Input ONNX path
        self.onnx_path = FilePath()
        self.engine_path = FilePath()
        self.export_log_path = FilePath()

        self.export_log = ConfigFile()

        self.use_fp32 = True
        self.use_fp16 = False

        self.static_shape = []
        self.dynamic_min_shape = []
        self.dynamic_max_shape = []

        self.is_analysis = False
        self.is_convert_complete = False

        self.setupUi(self)

        # Init Widget Args
        self.disable_config_widgets()
        self.disable_datatype_widget()
        self.disable_export_setting_widgets()
        self.disable_start_widgets()

        self.MIN_WORKSPACE = 1  # GB
        self.MAX_WORKSPACE = self.MIN_WORKSPACE * 12  # GB

        self.curr_workspace = 2
        self.label_workspace_number.setText(str(self.curr_workspace))
        self.horizontalSlider_workspace.setValue(self.curr_workspace)

        self.deonnx = DeONNX()

        # Widget connect slot function
        self.lineEdit_output.editingFinished.connect(self.lineEdit_output_editingFinished)
        self.horizontalSlider_workspace.valueChanged.connect(self.slider_workspace_valueChanged)

        self.radioButton_fp32.toggled.connect(self.on_radioButton_fp32_16_toggled)
        self.radioButton_fp16.toggled.connect(self.on_radioButton_fp32_16_toggled)

        self.lineEdit_max_shape.editingFinished.connect(self.lineEdit_min_shape_editingFinished)
        self.lineEdit_min_shape.editingFinished.connect(self.lineEdit_max_shape_editingFinished)

    def disable_config_widgets(self) -> None:

        self.lineEdit_onnx_input.setEnabled(False)
        self.lineEdit_output.setEnabled(False)

        self.pushButton_output.setEnabled(False)
        self.horizontalSlider_workspace.setEnabled(False)

    def disable_datatype_widget(self) -> None:
        # Datatype btns
        self.use_fp32 = True
        self.use_fp16 = True

        self.radioButton_fp32.setChecked(True)
        self.radioButton_fp16.setChecked(False)

        self.radioButton_fp32.setEnabled(False)
        self.radioButton_fp16.setEnabled(False)

    def disable_export_setting_widgets(self) -> None:
        self.lineEdit_model_type.setEnabled(False)
        self.lineEdit_min_shape.setEnabled(False)
        self.lineEdit_max_shape.setEnabled(False)

    def disable_start_widgets(self) -> None:
        self.pushButton_analysis_onnx.setEnabled(False)
        self.pushButton_run.setEnabled(True)

    @pyqtSlot()
    def on_pushButton_onnx_input_clicked(self) -> None:
        file_path, _ = QFileDialog.getOpenFileName(self, "选择文件", "/", 'onnx(*.onnx)')
        if file_path == '':
            return

        self.onnx_path.path = file_path
        self.onnx_path.decode()

        self.engine_path.path = os.path.join(
            self.onnx_path.dir,
            self.onnx_path.basename.replace(self.onnx_path.suffix, '.engine')
        )
        self.engine_path.decode()

        self.export_log_path.path = os.path.join(
            self.engine_path.dir,
            self.engine_path.basename.replace(self.engine_path.suffix, '.log.json')
        )
        self.export_log_path.decode()

        logger.info(f'ONNX FilePath: \n{self.onnx_path}')
        logger.info(f'Engine FilePath: \n{self.engine_path}')
        logger.info(f'Export Log FilePath: \n{self.export_log_path}')

        # Config widgets
        self.lineEdit_onnx_input.setText(self.onnx_path.path)
        self.lineEdit_output.setText(self.engine_path.path)

        self.pushButton_output.setEnabled(True)

        self.lineEdit_onnx_input.setReadOnly(True)
        self.lineEdit_output.setReadOnly(False)

        self.lineEdit_onnx_input.setEnabled(True)
        self.lineEdit_output.setEnabled(True)

        self.disable_datatype_widget()
        self.disable_export_setting_widgets()
        self.disable_start_widgets()

        # Clear lineedit text context
        self.lineEdit_model_type.setText('')
        self.lineEdit_min_shape.setText('')
        self.lineEdit_max_shape.setText('')
        self.textEdit_onnx_info.setText('')

        self.pushButton_analysis_onnx.setEnabled(True)

    @pyqtSlot()
    def on_pushButton_output_clicked(self) -> None:

        select_dir = QFileDialog.getExistingDirectory(self, "选择目录", "/")
        if select_dir == '':
            return

        self.engine_path.path = os.path.join(
            select_dir,
            self.onnx_path.basename.replace(self.onnx_path.suffix, '.engine')
        )
        self.engine_path.decode()

        self.export_log_path.path = os.path.join(
            self.engine_path.dir,
            self.engine_path.basename.replace(self.engine_path.suffix, '.log.json')
        )
        self.export_log_path.decode()

        self.lineEdit_output.setText(self.engine_path.path)

        logger.info(f'Engine FilePath: \n{self.engine_path}')
        logger.info(f'Export Log FilePath: \n{self.export_log_path}')

    def lineEdit_output_editingFinished(self) -> None:

        if os.path.isdir(self.lineEdit_output.text()):

            self.engine_path.path = os.path.join(
                self.lineEdit_output.text(),
                self.engine_path.basename
            )

        else:
            self.engine_path.path = self.lineEdit_output.text()

        self.engine_path.decode()

        self.export_log_path.path = os.path.join(
            self.engine_path.dir,
            self.engine_path.basename.replace(self.engine_path.suffix, '.log.json')
        )
        self.export_log_path.decode()

        logger.info(f'Engine FilePath: \n{self.engine_path}')
        logger.info(f'Export Log FilePath: \n{self.export_log_path}')

    @pyqtSlot()
    def on_pushButton_analysis_onnx_clicked(self):
        if not os.path.exists(self.onnx_path.path):
            QMessageBox.warning(self, 'Warning', 'Select Your ONNX Model.')
            return

        self.deonnx.set_onnx_path(self.onnx_path.path)
        self.deonnx.init()

        # Set lineedit text color
        palette = self.lineEdit_model_type.palette()
        palette.setColor(QPalette.Text, QColor(*self.colors.BiShanGreen))
        self.lineEdit_model_type.setPalette(palette)
        self.lineEdit_min_shape.setPalette(palette)
        self.lineEdit_max_shape.setPalette(palette)

        onnx_input = self.deonnx.inputs[0]
        onnx_input_shape = list2str(onnx_input.shape)

        if self.deonnx.is_dynamic:

            self.lineEdit_model_type.setText('Dynamic')

            self.lineEdit_min_shape.setEnabled(True)
            self.lineEdit_max_shape.setEnabled(True)

            self.lineEdit_min_shape.setReadOnly(False)
            self.lineEdit_max_shape.setReadOnly(False)

        else:
            self.lineEdit_model_type.setText('Static')

            self.lineEdit_min_shape.setEnabled(False)
            self.lineEdit_max_shape.setEnabled(False)

            self.lineEdit_min_shape.setReadOnly(True)
            self.lineEdit_max_shape.setReadOnly(True)

        self.lineEdit_min_shape.setText(onnx_input_shape)
        self.lineEdit_max_shape.setText(onnx_input_shape)

        self.radioButton_fp32.setEnabled(True)
        self.radioButton_fp16.setEnabled(True)
        self.radioButton_fp32.setChecked(True)
        self.radioButton_fp16.setChecked(False)

        self.horizontalSlider_workspace.setEnabled(True)

        palette = self.textEdit_onnx_info.palette()
        palette.setColor(QPalette.Text, QColor(*self.colors.PeacockBlue))
        self.textEdit_onnx_info.setPalette(palette)
        self.textEdit_onnx_info.setFontPointSize(12)
        self.textEdit_onnx_info.clear()
        self.textEdit_onnx_info.setText(self.deonnx.get_io_info())

        self.lineEdit_model_type.setEnabled(True)
        self.lineEdit_min_shape.setEnabled(True)
        self.lineEdit_max_shape.setEnabled(True)

        self.pushButton_run.setEnabled(True)

        self.is_analysis = True

    @pyqtSlot()
    def on_pushButton_run_clicked(self):

        logger.info('Click Run Button.')

        # try:
        #     import tensorrt
        # except:
        #     warning_info = 'Don`t fond the python tensorrt.'
        #     logger.warning(warning_info)
        #     QMessageBox.warning(self, 'Warning', warning_info)
        #     return

        export_args = {
            "workspace_size": self.curr_workspace,
        }
        # export_args = {
        #     "onnx_path": self.onnx_path.path,
        #     "output_path": self.engine_path.path,
        #     "fp32": self.radioButton_fp32.isChecked(),
        #     "fp16": self.radioButton_fp16.isChecked(),
        #     "is_dynamic:": self.deonnx.is_dynamic,
        #     "static_shape:": str2list(self.lineEdit_min_shape.text()),
        #     "input_name:": self.deonnx.inputs[0].name,
        #     "dynamic_min_shape": str2list(self.lineEdit_min_shape.text()),
        #     "dynamic_max_shape": str2list(self.lineEdit_max_shape.text()),
        #     "workspace_size": self.curr_workspace,
        # }

        self.export_thread.start()
        time.sleep(0.5)
        self.export_thread.args_signal.emit(export_args)
        self.export_thread.finished.connect(self.convert_progressbar.on_pushButton_stop_clicked)

        self.convert_progressbar.pushButton_stop.clicked.connect(self.export_thread.terminate)
        self.convert_progressbar.show()

        # self.export_log.add(export_args)
        # self.export_log.add({
        #     "export_time": get_time(),
        #     "uuid": self.config('uuid')
        # })
        # self.export_log.save(self.export_log_path.path)

    @pyqtSlot()
    def on_action_gitee_triggered(self):
        QDesktopServices.openUrl(QUrl(self.config('gitee')))

    @pyqtSlot()
    def on_action_github_triggered(self):
        QDesktopServices.openUrl(QUrl(self.config('github')))

    def slider_workspace_valueChanged(self):
        self.curr_workspace = self.horizontalSlider_workspace.value()
        self.label_workspace_number.setText(str(self.horizontalSlider_workspace.value()))
        logger.info(f'Current Workspace val: {self.curr_workspace} GB.')

    def on_radioButton_fp32_16_toggled(self):
        self.use_fp32 = self.radioButton_fp32.isChecked()
        self.use_fp16 = self.radioButton_fp16.isChecked()

        logger.info(f'RadioButton FP32: {self.radioButton_fp32.isChecked()}')
        logger.info(f'RadioButton FP16: {self.radioButton_fp16.isChecked()}')

    def lineEdit_min_shape_editingFinished(self) -> None:
        logger.info(f'Min Shape: {self.lineEdit_min_shape.text()}')

    def lineEdit_max_shape_editingFinished(self) -> None:
        logger.info(f'Max Shape: {self.lineEdit_max_shape.text()}')

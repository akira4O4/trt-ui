import os

from loguru import logger

from PyQt5.QtCore import QUrl
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox

from utils.utils import get_time
from utils.jsonconfig import JsonConfig
from utils.decode_onnx import DecodeONNX
# from utils.onnx2engine import ONNX2Engine
from ui.ui_onnx2engine import Ui_ONNX2Engine
from slot.slot_convert import SlotConvert


class SlotONNX2Engine(QMainWindow, Ui_ONNX2Engine):
    def __init__(self, config_path: str) -> None:
        super().__init__()
        self.config = JsonConfig(config_path)

        # Input ONNX path
        self.onnx_model_path = ''
        self.onnx_model_dir = ''
        self.onnx_model_name = ''

        # Output Engine Path info
        self.engine_model_name = ''
        self.engine_model_dir = ''
        self.engine_model_path = ''

        # Import And Export Config Path
        self.import_config_path = ''
        self.import_config_data: JsonConfig = None

        self.export_config_path = ''
        self.export_config_data: JsonConfig = None

        self.datatype = 'FP32'
        self.use_fp32 = True
        self.use_fp16 = False

        self.static_shape = []
        self.dynamic_min_shape = []
        self.dynamic_max_shape = []

        self.is_analysis = False
        self.is_convert_complete = False

        self.setupUi(self)

        # Init Widget Args
        self.radioButton_fp32.setEnabled(False)
        self.radioButton_fp16.setEnabled(False)

        # GB
        self.MIN_WORKSPACE = 2
        self.MAX_WORKSPACE = self.MIN_WORKSPACE * 12

        self.curr_workspace = self.MIN_WORKSPACE
        self.label_workspace_number.setText(str(self.MIN_WORKSPACE))
        self.horizontalSlider_workspace.setValue(self.MIN_WORKSPACE)

        self.model_type = 'static'
        self.lineEdit_model_type.setEnabled(False)
        self.lineEdit_min_shape.setEnabled(False)
        self.lineEdit_max_shape.setEnabled(False)

        self.decode_onnx = DecodeONNX()

        self.horizontalSlider_workspace.valueChanged.connect(self.slider_workspace)

    @staticmethod
    def split_path(path: str) -> dict:

        file_dir = ''
        basename = ''

        if os.path.isdir(path):
            file_dir, basename = os.path.split(path)
        else:
            basename = path

        name, suffix = os.path.splitext(basename)
        return {'file_dir': file_dir, 'basename': basename, 'name': name, 'suffix': suffix}

    @staticmethod
    def str2list(data: str) -> list:
        if not data:
            return []
        try:
            _data = data.split(',')
            _data = [int(x) for x in _data]
            return _data
        except:
            logger.error('Input Data Error.')
            return []

    @staticmethod
    def list2str(data: list) -> str:
        if len(data) == 0:
            return ''
        return ','.join(map(str, data))

    @pyqtSlot()
    def on_pushButton_onnx_input_clicked(self) -> None:
        file_path, _ = QFileDialog.getOpenFileName(self, "选择文件", "/", 'onnx(*.onnx)')
        if file_path == '':
            return

        self.radioButton_fp32.setEnabled(False)
        self.radioButton_fp16.setEnabled(False)
        self.lineEdit_model_type.setEnabled(False)
        self.lineEdit_min_shape.setEnabled(False)
        self.lineEdit_max_shape.setEnabled(False)

        file_info = self.split_path(file_path)

        self.onnx_model_path = file_path
        self.onnx_model_dir = file_info['file_dir']
        self.onnx_model_name = file_info['basename']
        name = file_info['name']
        suffix = file_info['suffix']

        if suffix.lower() != '.onnx':
            logger.error('Input model is not ONNX file.')

        self.engine_model_name = name + '.engine'
        self.engine_model_path = os.path.join(self.onnx_model_dir, self.engine_model_name)

        self.lineEdit_onnx_input.setText(self.onnx_model_path)
        self.lineEdit_output.setText(self.engine_model_path)

        logger.info(f'Select ONNX: {self.onnx_model_path}')

    @pyqtSlot()
    def on_pushButton_output_clicked(self) -> None:

        self.engine_model_dir = QFileDialog.getExistingDirectory(self, "选择目录", "/")
        if self.engine_model_dir == '':
            return

        self.lineEdit_output.setText(self.engine_model_dir)
        logger.info(f'Select Output Dir: {self.engine_model_dir}')

    @pyqtSlot()
    def on_pushButton_input_config_clicked(self) -> None:
        self.import_config_path, _ = QFileDialog.getOpenFileName(self, "选择文件", "/", 'json(*.json)')
        if self.import_config_path == '':
            return
        file_info = self.split_path(self.import_config_path)
        if file_info['suffix'].lower() != '.json':
            logger.error(f'Input config file is not json file.')

        self.import_config_data = JsonConfig(self.import_config_path)

        self.lineEdit_onnx_input.setText(self.import_config_data('onnx_model'))
        self.lineEdit_output.setText(self.import_config_data('engine_model'))
        self.lineEdit_input_config.setText(self.import_config_path)

        self.label_workspace_number.setText(str(self.import_config_data('workspace')))

        if self.import_config_data('fp32'):
            self.radioButton_fp32.setChecked(True)
            self.radioButton_fp16.setChecked(False)
        else:
            self.radioButton_fp32.setChecked(False)
            self.radioButton_fp16.setChecked(True)

        self.lineEdit_model_type.setText(self.import_config_data('model_type'))
        if self.import_config_data('model_type').lower() == 'static':
            self.lineEdit_min_shape.setText(self.list2str(self.import_config_data('min_shape')))
            # self.lineEdit_mid_shape.setText(self.list2str(self.import_config_data('min_shape')))
            self.lineEdit_max_shape.setText(self.list2str(self.import_config_data('min_shape')))
        else:
            self.lineEdit_min_shape.setText(self.list2str(self.import_config_data('min_shape')))
            # self.lineEdit_mid_shape.setText(self.list2str(self.import_config_data('mid_shape')))
            self.lineEdit_max_shape.setText(self.list2str(self.import_config_data('max_shape')))

        logger.info(f'Select Model Config: {self.export_config_path}')

    @pyqtSlot()
    def on_pushButton_analysis_onnx_clicked(self):
        if not os.path.exists(self.onnx_model_path):
            QMessageBox.warning(self, 'Warning', 'Select Your ONNX Model.')
            return

        self.is_analysis = True

        self.radioButton_fp32.setEnabled(True)
        self.radioButton_fp16.setEnabled(True)

        self.lineEdit_model_type.setEnabled(True)
        self.lineEdit_min_shape.setEnabled(True)
        self.lineEdit_max_shape.setEnabled(True)

        self.decode_onnx.set_onnx_path(self.onnx_model_path)
        self.decode_onnx.init()
        self.decode_onnx.decode_io()

        if self.decode_onnx.is_dynamic:
            onnx_input = self.decode_onnx.inputs[0]
            onnx_input_shape = self.list2str(onnx_input.shape)

            self.lineEdit_model_type.setText('Dynamic')
            self.lineEdit_min_shape.setText(onnx_input_shape)
            self.lineEdit_max_shape.setText(onnx_input_shape)
            self.lineEdit_min_shape.setReadOnly(True)
            self.lineEdit_max_shape.setReadOnly(True)
        else:
            onnx_input = self.decode_onnx.inputs[0]
            onnx_input_shape = self.list2str(onnx_input.shape)

            self.lineEdit_model_type.setText('Static')
            self.lineEdit_min_shape.setText(onnx_input_shape)
            self.lineEdit_max_shape.setText(onnx_input_shape)
            self.lineEdit_min_shape.setReadOnly(True)
            self.lineEdit_max_shape.setReadOnly(True)
        self.textEdit_onnx_info.setText(self.decode_onnx.get_io_info())

    @pyqtSlot()
    def on_pushButton_export_config_clicked(self) -> None:
        if not self.is_analysis:
            QMessageBox.warning(self, "Warning", "Please Use Auto Analysis Function.")
            return

        filepath, _ = QFileDialog.getSaveFileName(self, '文件保存', '/', 'json(*.json)')
        if filepath == '':
            return

        export_args = {
            "onnx_model": self.onnx_model_path,
            "engine_model": self.engine_model_path,
            "workspace": self.curr_workspace,
            "fp32": self.radioButton_fp32.isChecked(),
            "fp16": self.radioButton_fp16.isChecked(),
            "model_type": self.lineEdit_model_type.text(),
            "min_shape": self.str2list(self.lineEdit_min_shape.text()),
            # "mid_shape": self.str2list(self.lineEdit_mid_shape.text()),
            "max_shape": self.str2list(self.lineEdit_max_shape.text()),
            "export_time": get_time(),
            "uuid": self.config('uuid')
        }

        export_config = JsonConfig()
        export_config.data = export_args
        export_config.save(filepath)
        QMessageBox.information(self, 'Success', 'Export Model Config Success.')

    # @pyqtSlot()
    def on_pushButton_run_clicked(self):
        ui_convert = SlotConvert()
        ui_convert.show()

        if self.radioButton_fp32.isChecked():
            self.use_fp32 = True
            self.use_fp16 = False
        if self.radioButton_fp16.isChecked():
            self.use_fp32 = False
            self.use_fp16 = True

        if not self.is_analysis:
            QMessageBox.warning(self, "Warning", "Please Use Analysis Function.")
        else:

            # ui_convert = SlotConvert()
            # ui_convert.show()

            static_shape = None
            dynamic_min_shape = None
            dynamic_max_shape = None

            if self.decode_onnx.is_dynamic:
                static_shape = self.str2list(self.lineEdit_min_shape)
            else:
                dynamic_min_shape = self.str2list(self.lineEdit_min_shape)
                dynamic_max_shape = self.str2list(self.lineEdit_max_shape)

            # onnx2engine = ONNX2Engine(
            #     self.onnx_model_path,
            #     self.engine_model_path,
            #     self.use_fp32,
            #     self.use_fp16,
            #     self.decode_onnx.is_dynamic,
            #     static_shape,
            #     self.decode_onnx.get_input(0).name,
            #     dynamic_min_shape,
            #     dynamic_max_shape,
            #     self.curr_workspace
            # )
            # onnx2engine.init()
            # flag = onnx2engine.run()
            # if flag:
            #     QMessageBox.information(self, "Success", "Completed Creating Engine")

    @pyqtSlot()
    def on_action_gitee_triggered(self):
        QDesktopServices.openUrl(QUrl(self.config('github')))

    @pyqtSlot()
    def on_action_github_triggered(self):
        QDesktopServices.openUrl(QUrl(self.config('gitee')))

    def slider_workspace(self):
        self.curr_workspace = self.horizontalSlider_workspace.value()
        self.label_workspace_number.setText(str(self.horizontalSlider_workspace.value()))
        logger.info(self.curr_workspace)

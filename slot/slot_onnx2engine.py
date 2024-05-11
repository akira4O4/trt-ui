import os

from loguru import logger

from PyQt5.QtCore import QUrl
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QDesktopServices, QColor, QPalette
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox

from utils.utils import get_time
from utils.jsonfile import JsonFile
from utils.decode_onnx import DecodeONNX
from utils.colors import Colors
# from utils.onnx2engine import ONNX2Engine
from ui.ui_onnx2engine import Ui_ONNX2Engine
from slot.slot_convert import SlotConvert


class SlotONNX2Engine(QMainWindow, Ui_ONNX2Engine):
    def __init__(self, config_path: str) -> None:
        super().__init__()
        self.config = JsonFile(config_path)
        self.export_log = JsonFile('configs/export.log.json')
        self.export_log_path = ''
        self.colors = Colors
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
        self.import_config_data: JsonFile = None

        self.export_config_path = ''
        self.export_config_data: JsonFile = None

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

        self.radioButton_fp32.setEnabled(False)
        self.radioButton_fp16.setEnabled(False)

        self.MIN_WORKSPACE = 1  # GB
        self.MAX_WORKSPACE = self.MIN_WORKSPACE * 12  # GB

        self.curr_workspace = 2
        self.label_workspace_number.setText(str(self.curr_workspace))
        self.horizontalSlider_workspace.setValue(self.curr_workspace)

        self.model_type = 'static'
        self.lineEdit_model_type.setEnabled(False)
        self.lineEdit_min_shape.setEnabled(False)
        self.lineEdit_max_shape.setEnabled(False)

        self.decode_onnx = DecodeONNX()

        # Widget connect slot function
        self.horizontalSlider_workspace.valueChanged.connect(self.slider_workspace)
        self.lineEdit_output.editingFinished.connect(self.lineEdit_output_editingFinished)
        self.radioButton_fp32.toggled.connect(self.on_radioButton_fp32_toggled)

    def disable_config_widgets(self) -> None:
        self.lineEdit_output.setReadOnly(True)
        self.lineEdit_input_config.setReadOnly(True)
        self.lineEdit_input_config.setReadOnly(True)

        self.lineEdit_onnx_input.setEnabled(False)
        self.lineEdit_output.setEnabled(False)
        self.lineEdit_input_config.setEnabled(False)

        self.pushButton_output.setEnabled(False)
        self.pushButton_input_config.setEnabled(False)

    def disable_datatype_widget(self) -> None:
        # Datatype btns
        self.use_fp32 = True
        self.use_fp16 = True

        self.radioButton_fp32.setChecked(True)
        self.radioButton_fp16.setChecked(False)

        self.radioButton_fp32.setEnabled(False)
        self.radioButton_fp16.setEnabled(False)

    def disable_export_setting_widgets(self) -> None:
        self.lineEdit_model_type.setReadOnly(True)
        self.lineEdit_min_shape.setReadOnly(True)
        self.lineEdit_max_shape.setReadOnly(True)

        self.lineEdit_model_type.setEnabled(False)
        self.lineEdit_min_shape.setEnabled(False)
        self.lineEdit_max_shape.setEnabled(False)

    def disable_start_widgets(self) -> None:
        self.pushButton_analysis_onnx.setEnabled(False)
        self.pushButton_export_config.setEnabled(False)
        self.pushButton_run.setEnabled(False)

    @staticmethod
    def split_path(path: str) -> dict:

        file_dir = ''
        basename = ''

        if os.path.isdir(path):
            file_dir, basename = os.path.split(path)
        else:
            basename = path

        name, suffix = os.path.splitext(basename)
        return {
            'file_dir': file_dir,
            'basename': basename,
            'name': name,
            'suffix': suffix
        }

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

        self.onnx_model_path = file_path
        self.onnx_model_dir, self.onnx_model_name = os.path.split(file_path)

        self.engine_model_name = self.onnx_model_name.replace('onnx', 'engine')
        self.engine_model_dir = self.onnx_model_dir
        self.engine_model_path = os.path.join(self.engine_model_dir, self.engine_model_name)

        self.export_log_path = os.path.join(self.onnx_model_dir, self.onnx_model_name.replace('onnx', 'log.json'))
        logger.info(f'Export Log Path: {self.export_log_path}')
        # Config widgets
        self.lineEdit_onnx_input.setText(self.onnx_model_path)
        self.lineEdit_output.setText(self.engine_model_path)

        self.pushButton_output.setEnabled(True)
        self.pushButton_input_config.setEnabled(True)

        self.lineEdit_onnx_input.setReadOnly(True)
        self.lineEdit_output.setReadOnly(False)
        self.lineEdit_input_config.setReadOnly(True)

        self.lineEdit_onnx_input.setEnabled(True)
        self.lineEdit_output.setEnabled(True)
        self.lineEdit_input_config.setEnabled(True)

        self.disable_datatype_widget()
        self.disable_export_setting_widgets()
        self.disable_start_widgets()

        # Clear lineedit text context
        self.lineEdit_model_type.setText('')
        self.lineEdit_min_shape.setText('')
        self.lineEdit_max_shape.setText('')
        self.textEdit_onnx_info.setText('')

        self.pushButton_analysis_onnx.setEnabled(True)

        logger.info(f'Select ONNX Path: {self.onnx_model_path}')
        logger.info(f'Select ONNX Dir: {self.onnx_model_dir}')
        logger.info(f'Select ONNX Name: {self.onnx_model_name}')
        logger.info(f'Create Engine Path: {self.engine_model_path}')
        logger.info(f'Create Engine Dir: {self.engine_model_dir}')
        logger.info(f'Create Engine Name: {self.engine_model_name}')

    @pyqtSlot()
    def on_pushButton_output_clicked(self) -> None:

        select_dir = QFileDialog.getExistingDirectory(self, "选择目录", "/")
        if select_dir == '':
            return

        self.engine_model_dir = select_dir
        self.engine_model_path = os.path.join(self.engine_model_dir, self.onnx_model_name.replace('onnx', 'engine'))

        self.lineEdit_output.setText(self.engine_model_path)
        logger.info(f'Engine Output Path: {self.engine_model_path}')
        logger.info(f'Engine Output Dir: {self.engine_model_dir}')
        logger.info(f'Engine Output Name: {self.engine_model_name}')

    def lineEdit_output_editingFinished(self) -> None:
        if os.path.isdir(self.lineEdit_output.text()):
            self.engine_model_dir = self.lineEdit_output.text()
            self.engine_model_path = os.path.join(self.engine_model_dir, self.engine_model_name)

        else:
            self.engine_model_path = self.lineEdit_output.text()
            self.engine_model_dir, self.engine_model_name = os.path.split(self.engine_model_path)
            logger.info(f'Engine Output Path: {self.engine_model_path}')
            logger.info(f'Engine Output Dir: {self.engine_model_dir}')
            logger.info(f'Engine Output Name: {self.engine_model_name}')

    # TODO
    @pyqtSlot()
    def on_pushButton_input_config_clicked(self) -> None:
        self.import_config_path, _ = QFileDialog.getOpenFileName(self, "选择文件", "/", 'json(*.json)')
        if self.import_config_path == '':
            return

        self.import_config_data = JsonFile(self.import_config_path)

        self.lineEdit_input_config.setText(self.import_config_path)
        self.horizontalSlider_workspace.setValue(self.import_config_data('workspace'))
        self.label_workspace_number.setText(str(self.import_config_data('workspace')))

        if self.import_config_data('fp32'):
            self.radioButton_fp32.setChecked(True)
            self.radioButton_fp16.setChecked(False)
        else:
            self.radioButton_fp32.setChecked(False)
            self.radioButton_fp16.setChecked(True)

        self.lineEdit_model_type.setText(self.import_config_data('model_type'))
        if self.import_config_data('model_type').lower() == 'static':
            self.lineEdit_min_shape.setText(self.list2str(self.import_config_data('input_min_shape')))
            self.lineEdit_max_shape.setText(self.list2str(self.import_config_data('input_min_shape')))
        else:
            self.lineEdit_min_shape.setText(self.list2str(self.import_config_data('input_min_shape')))
            self.lineEdit_max_shape.setText(self.list2str(self.import_config_data('input_max_shape')))

        logger.info(f'Select Model Config: {self.import_config_path}')

    @pyqtSlot()
    def on_pushButton_analysis_onnx_clicked(self):
        if not os.path.exists(self.onnx_model_path):
            QMessageBox.warning(self, 'Warning', 'Select Your ONNX Model.')
            return

        self.decode_onnx.set_onnx_path(self.onnx_model_path)
        self.decode_onnx.init()
        self.decode_onnx.decode_io()

        # Set lineedit text color
        palette = self.lineEdit_model_type.palette()
        palette.setColor(QPalette.Text, QColor(*self.colors.BiShanGreen))
        self.lineEdit_model_type.setPalette(palette)
        self.lineEdit_min_shape.setPalette(palette)
        self.lineEdit_max_shape.setPalette(palette)

        onnx_input = self.decode_onnx.inputs[0]
        onnx_input_shape = self.list2str(onnx_input.shape)

        if self.decode_onnx.is_dynamic:

            self.lineEdit_model_type.setText('Dynamic')

            self.lineEdit_min_shape.setReadOnly(False)
            self.lineEdit_max_shape.setReadOnly(False)
        else:
            self.lineEdit_model_type.setText('Static')

            self.lineEdit_min_shape.setReadOnly(True)
            self.lineEdit_max_shape.setReadOnly(True)

        self.lineEdit_min_shape.setText(onnx_input_shape)
        self.lineEdit_max_shape.setText(onnx_input_shape)

        self.radioButton_fp32.setEnabled(True)
        self.radioButton_fp16.setEnabled(True)
        self.radioButton_fp32.setChecked(True)
        self.radioButton_fp16.setChecked(False)

        palette = self.textEdit_onnx_info.palette()
        palette.setColor(QPalette.Text, QColor(*self.colors.PeacockBlue))
        self.textEdit_onnx_info.setPalette(palette)
        self.textEdit_onnx_info.setFontPointSize(12)
        self.textEdit_onnx_info.clear()
        self.textEdit_onnx_info.setText(self.decode_onnx.get_io_info())

        self.lineEdit_model_type.setEnabled(True)
        self.lineEdit_min_shape.setEnabled(True)
        self.lineEdit_max_shape.setEnabled(True)

        self.pushButton_export_config.setEnabled(True)
        self.pushButton_run.setEnabled(True)

        self.is_analysis = True

    @pyqtSlot()
    def on_pushButton_export_config_clicked(self) -> None:
        if not self.is_analysis:
            QMessageBox.warning(self, "Warning", "Please Use Auto Analysis Function.")
            return

        filepath, _ = QFileDialog.getSaveFileName(self, '文件保存', '/', 'json(*.json)')
        if filepath == '':
            return
        self.export_config.add({
            "workspace": self.curr_workspace,
            "fp32": self.radioButton_fp32.isChecked(),
            "fp16": self.radioButton_fp16.isChecked(),
            "model_type": self.lineEdit_model_type.text(),
            "input_min_shape": self.str2list(self.lineEdit_min_shape.text()),
            "input_max_shape": self.str2list(self.lineEdit_max_shape.text()),
            "export_time": get_time(),
            "uuid": self.config('uuid')
        })
        self.export_config.save(filepath)
        QMessageBox.information(self, 'Success', 'Export Model Config Success.')

    @pyqtSlot()
    def on_pushButton_run_clicked(self):
        logger.info('Click Run Button.')
        self.export_log.add({
            "input_onnx_path": self.onnx_model_path,
            "output_engine_path": self.engine_model_path,
            "workspace": self.curr_workspace,
            "fp32": self.radioButton_fp32.isChecked(),
            "fp16": self.radioButton_fp16.isChecked(),
            "model_type": self.lineEdit_model_type.text(),
            "input_min_shape": self.str2list(self.lineEdit_min_shape.text()),
            "input_max_shape": self.str2list(self.lineEdit_max_shape.text()),
            "export_time": get_time(),
            "uuid": self.config('uuid')
        })

        self.export_log.save(self.export_log_path)
        # ui_convert = SlotConvert()
        # ui_convert.show()

        # if self.radioButton_fp32.isChecked():
        #     self.use_fp32 = True
        #     self.use_fp16 = False
        # if self.radioButton_fp16.isChecked():
        #     self.use_fp32 = False
        #     self.use_fp16 = True
        #
        # if not self.is_analysis:
        #     QMessageBox.warning(self, "Warning", "Please Use Analysis Function.")
        # else:
        #
        # ui_convert = SlotConvert()
        # ui_convert.show()
        #
        # static_shape = None
        # dynamic_min_shape = None
        # dynamic_max_shape = None
        #
        # if self.decode_onnx.is_dynamic:
        #     static_shape = self.str2list(self.lineEdit_min_shape)
        # else:
        #     dynamic_min_shape = self.str2list(self.lineEdit_min_shape)
        #     dynamic_max_shape = self.str2list(self.lineEdit_max_shape)
        #
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
        logger.info(f'Current Workspace val: {self.curr_workspace}')

    def on_radioButton_fp32_toggled(self):
        if self.radioButton_fp32.isChecked():
            self.use_fp32 = True
            self.use_fp16 = False

        elif self.radioButton_fp16.isChecked():
            self.use_fp32 = False
            self.use_fp16 = True

        logger.info(f'RadioButton FP32: {self.radioButton_fp32.isChecked()}')
        logger.info(f'RadioButton FP16: {self.radioButton_fp16.isChecked()}')

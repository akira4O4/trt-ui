from loguru import logger
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot, QObject
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from views.py.ui_convert_progress_bar import Ui_Convert


class ConvertProgressBar(QMainWindow, Ui_Convert):
    stop_signal = QtCore.pyqtSignal()

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

    @pyqtSlot()
    def on_pushButton_stop_clicked(self):
        # logger.info('Close Progress Bar.')
        logger.info('Emit Stop Signal.')
        self.stop_signal.emit()
        self.close()

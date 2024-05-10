from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from ui.ui_convert import Ui_Convert


class SlotConvert(QMainWindow, Ui_Convert):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.progressBar_convert.setRange(0, 100)
        self.progressBar_convert.setMinimum(0)
        self.progressBar_convert.setMaximum(100)

    @pyqtSlot()
    def on_pushButton_stop_clicked(self):
        self.close()

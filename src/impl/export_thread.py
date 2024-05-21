import time

from loguru import logger
from PyQt5 import QtCore
from PyQt5.QtCore import QThread, pyqtSignal, QObject


class ExportEngineWork(QObject):
    finished_signal = QtCore.pyqtSignal()
    stop_flag = False

    def __init__(self):
        super().__init__()
        # self.args = {}

    def run(self, args: dict):
        if args != {}:
            logger.info(f'Export Args: {args}')
            logger.info(f'Work Thread Running.')
            for i in range(5):
                time.sleep(0.5)
                print(i)
            self.finished_signal.emit()
            logger.info(f'Export Thread Emit Finished Signal.')

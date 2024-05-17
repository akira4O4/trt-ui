import time

from loguru import logger
from PyQt5.QtCore import QThread, pyqtSignal
from src.impl.convert_progressbar import ConvertProgressBar


class ExportThread(QThread):
    args_signal = pyqtSignal(dict)

    def __init__(self):
        super(ExportThread, self).__init__()
        self.args_signal.connect(self.recv_args)
        # self.args_signal.connect(self.something)
        self.args = {}

    def run(self):
        logger.info(f'Run RunThread')
        print(self.args)

    def recv_args(self, args: dict) -> None:
        logger.info('Recv Args.')
        self.args = args

    def something(self):
        for i in range(100):
            time.sleep(0.1)
            print(i)

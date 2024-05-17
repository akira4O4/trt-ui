import time

from loguru import logger
from PyQt5.QtCore import QThread, pyqtSignal


class ExportThread(QThread):
    args_signal = pyqtSignal(dict)

    def __init__(self):
        super(ExportThread, self).__init__()
        self.args_signal.connect(self.recv_args)
        self.args = {}

    def run(self):
        logger.info(f'Run RunThread')
        print(self.args)
        for i in range(100):
            time.sleep(0.1)
            print(i)

    def recv_args(self, args: dict) -> None:
        logger.info('Recv Args.')
        self.args = args

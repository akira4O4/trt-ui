import os
import sys
from PyQt5 import QtWidgets
from loguru import logger
from utils.utils import get_uuid, get_time
from utils.jsonfile import JsonFile
from utils.decode_onnx import DecodeONNX
from slot.slot_onnx2engine import SlotONNX2Engine

if __name__ == '__main__':

    # Install app version.json

    config = JsonFile('configs/version.json')
    install_config_dir = os.path.join(os.path.expanduser("~"), f".config/{config('app_name')}")
    install_config_path = os.path.join(install_config_dir, 'version.json')

    if not os.path.exists(install_config_path):
        if not os.path.exists(install_config_dir):
            os.makedirs(install_config_dir)

        if not os.path.exists(install_config_path):
            config.add({'install_time': get_time()})
            config.add({'uuid': get_uuid()})
            config.save(install_config_path)
            logger.success(f'Install config to: {install_config_path}')

    app = QtWidgets.QApplication(sys.argv)
    window = SlotONNX2Engine(install_config_path)
    window.show()
    sys.exit(app.exec())

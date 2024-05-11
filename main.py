import os
import sys
from PyQt5 import QtWidgets
from loguru import logger
from utils.utils import get_uuid, get_time
from utils.jsonconfig import JsonConfig
from utils.decode_onnx import DecodeONNX
from slot.slot_onnx2engine import SlotONNX2Engine

if __name__ == '__main__':

    # Install app version.json
    default_config_dir = os.path.join(os.path.expanduser("~"), r".config/export-ui")
    if not os.path.exists(default_config_dir):
        os.makedirs(default_config_dir)
    default_config_path = os.path.join(default_config_dir, 'version.json')
    config = None
    if not os.path.exists(default_config_path):
        config = JsonConfig('configs/version.json')
        config.add({'install_time': get_time()})
        config.add({'uuid': get_uuid()})
        config.save(default_config_path)
        logger.success(f'Install config to: {default_config_path}')

    app = QtWidgets.QApplication(sys.argv)
    window = SlotONNX2Engine(default_config_path)
    window.show()
    sys.exit(app.exec())

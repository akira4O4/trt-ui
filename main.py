import os
import sys
from PyQt6 import QtWidgets

from utils.utils import get_uuid, get_time
from utils.jsonconfig import JsonConfig
from utils.decode_onnx import DecodeONNX
from call.onnx2engine import CallONNX2Engine


if __name__ == '__main__':
    # decode_onnx=DecodeONNX(r'D:\llf\code\export-ui\temp\20240421_201659_danyang_E_mt_bs1_cls4_seg6_static.onnx')
    # print(decode_onnx.inputs)
    # print(decode_onnx.outputs)
    # print(decode_onnx.get_io_info())
    # exit()
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

    app = QtWidgets.QApplication(sys.argv)
    window = CallONNX2Engine(default_config_path)
    window.show()
    sys.exit(app.exec())

import os
import sys
from PyQt5 import QtWidgets
from loguru import logger
from src.utils import get_uuid, get_time
from src.jsonfile import JsonFile
from src.filepath import FilePath
from slot.slot_onnx2engine import SlotONNX2Engine


def get_home_dir() -> str:
    if sys.platform == 'win32':
        home_dir = os.environ['USERPROFILE']
    elif sys.platform == 'linux' or sys.platform == 'darwin':
        home_dir = os.environ['HOME']
    else:
        raise NotImplemented(f'Error! Not this system. {sys.platform}')
    return home_dir


_HOME_ = get_home_dir()

_DEFAULT_CONFIG_PATH_ = FilePath(r'configs/config.json')
_DEFAULT_CONFIG_ = JsonFile(_DEFAULT_CONFIG_PATH_.path)

_INSTALL_CONFIG_PATH_ = FilePath()
_INSTALL_CONFIG_ = JsonFile()


def init_logger() -> None:
    app_log_path = os.path.join(_INSTALL_CONFIG_PATH_.dir, 'app.log')
    logger.add(app_log_path)
    logger.info(f'APP Log File In: {app_log_path}.')


def init_app_config() -> None:
    # install_path: ~/.config/trt-export/config.json
    install_path = os.path.join(_HOME_, f".config/{_DEFAULT_CONFIG_('app_name')}/{_DEFAULT_CONFIG_PATH_.basename}")
    _INSTALL_CONFIG_PATH_.path = install_path
    _INSTALL_CONFIG_PATH_.decode()

    if not os.path.exists(_INSTALL_CONFIG_PATH_.path):
        if not os.path.exists(_INSTALL_CONFIG_PATH_.dir):
            os.makedirs(_INSTALL_CONFIG_PATH_.dir)
            logger.info(f'Make Dir: {_INSTALL_CONFIG_PATH_.dir}')

        _DEFAULT_CONFIG_.add({
            'install_time': get_time(),
            'uuid': get_uuid()
        })

    else:
        _INSTALL_CONFIG_.path = _INSTALL_CONFIG_PATH_.path
        _INSTALL_CONFIG_.load()
        _DEFAULT_CONFIG_.add({
            'install_time': get_time(),
            'uuid': _INSTALL_CONFIG_('uuid')
        })

    _DEFAULT_CONFIG_.save(_INSTALL_CONFIG_PATH_.path)
    logger.success(f'Install version.json to: {_INSTALL_CONFIG_PATH_.path}')


def app() -> None:
    application = QtWidgets.QApplication(sys.argv)
    window = SlotONNX2Engine(_INSTALL_CONFIG_PATH_.path)
    window.show()
    sys.exit(application.exec())


if __name__ == '__main__':
    init_app_config()
    init_logger()
    app()

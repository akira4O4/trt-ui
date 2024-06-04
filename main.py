import os
import sys

from loguru import logger
from PyQt5 import QtWidgets

from src import VERSION,HOME
from src.filepath import FilePath
from src.configfile import ConfigFile
from src.impl.onnx2engine import ONNX2Engine
from src.utils import get_uuid, get_time, get_home_dir

# _HOME_ = get_home_dir()

_DEFAULT_CONFIG_PATH_ = FilePath(r'configs/config.json')
_DEFAULT_CONFIG_ = ConfigFile(_DEFAULT_CONFIG_PATH_.path)

_INSTALL_CONFIG_PATH_ = FilePath()
_INSTALL_CONFIG_ = ConfigFile()


def init_logger_config() -> None:
    app_log_path = os.path.join(_INSTALL_CONFIG_PATH_.dir, 'app.log')
    logger.add(app_log_path)
    logger.info(f'APP Log File In: {app_log_path}.')


def init_app_config() -> None:
    # install_path: ~/.config/trt-export/config.json
    install_path = os.path.join(HOME, f".config/{_DEFAULT_CONFIG_('app_name')}/{_DEFAULT_CONFIG_PATH_.basename}")
    _INSTALL_CONFIG_PATH_.path = install_path
    _INSTALL_CONFIG_PATH_.decode()

    if not os.path.exists(_INSTALL_CONFIG_PATH_.path):
        if not os.path.exists(_INSTALL_CONFIG_PATH_.dir):
            os.makedirs(_INSTALL_CONFIG_PATH_.dir)
            logger.info(f'Make Dir: {_INSTALL_CONFIG_PATH_.dir}')

        _DEFAULT_CONFIG_.update({
            'install_time': get_time(),
            'uuid': get_uuid()
        })

    else:
        _INSTALL_CONFIG_.path = _INSTALL_CONFIG_PATH_.path
        _INSTALL_CONFIG_.load()
        _DEFAULT_CONFIG_.update({
            'install_time': get_time(),
            'uuid': _INSTALL_CONFIG_('uuid')
        })

    _DEFAULT_CONFIG_.save(_INSTALL_CONFIG_PATH_.path)
    logger.success(f'Install version.json to: {_INSTALL_CONFIG_PATH_.path}')


def app() -> None:
    application = QtWidgets.QApplication(sys.argv)
    window = ONNX2Engine(_INSTALL_CONFIG_PATH_.path)
    window.show()
    sys.exit(application.exec())


if __name__ == '__main__':
    logger.info(f'Version: {VERSION}')
    init_app_config()
    init_logger_config()
    app()

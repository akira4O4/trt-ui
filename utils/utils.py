import os
import json
import shutil
import uuid
import time
from loguru import logger


def check_ext(file: str, exts: list) -> bool:
    base_name = os.path.basename(file)
    _, ext = os.path.splitext(base_name)
    if ext not in exts:
        logger.error(f'{file} ext is not validate:f{exts}')
        return False
    return True


def load_json(path: str):
    data = None
    if not check_ext(path, ['.json']):
        return data
    with open(path, 'r') as config_file:
        data = json.load(config_file)  # 配置字典
    return data

def get_time(fmt: str = '%Y%m%d_%H%M%S') -> str:
    time_str = time.strftime(fmt, time.localtime())
    return str(time_str)


def get_uuid() -> str:
    return str(uuid.uuid1())

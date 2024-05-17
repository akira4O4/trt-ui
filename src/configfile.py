import os
import yaml
import json
from typing import Optional
from loguru import logger


class ConfigFile:
    def __init__(self, path: Optional[str] = None) -> None:
        self._path = path
        self._data = {}
        if path is not None:
            self.load()

    @property
    def data(self) -> dict:
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def path(self) -> str:
        return self._path

    @path.setter
    def path(self, value):
        self._path = value

    def load(self):
        base_name = os.path.basename(self._path)
        _, suffix = os.path.splitext(base_name)
        if suffix.lower() == '.yaml':
            self._load_yaml()
        elif suffix.lower() == '.json':
            self._load_json()

        else:
            logger.error('Input file is not yaml or json. ')
            exit()

    def _load_json(self) -> None:
        with open(self.path, 'r') as config_file:
            self.data = json.load(config_file)
        logger.info(f'Loading: {self.path}.')

    def _load_yaml(self) -> None:
        with open(self._path, encoding='utf-8') as f:
            self.data = yaml.load(f, Loader=yaml.FullLoader)
        logger.info(f'Loading: {self.path}.')

    def remove(self, key: str) -> bool:
        if self.data.get(key) is None:
            logger.error(f'Key: {key}is not found.')
            return False
        else:
            logger.info(f'Del {key}:{self.data[key]}.')
            del self.data[key]
            return True

    def add(self, kv: dict, overwrite: Optional[bool] = True):
        for k, v in kv.items():
            self._set(k, v, overwrite)

    def _set(self, key: str, val, overwrite: Optional[bool] = True):

        if self.data.get(key) is None or self.data.get(key) == "":
            self.data[key] = val
            logger.success(f'Set {key} : {val}')
        else:
            if overwrite:
                self.data[key] = val
                logger.success(f'Set {key}:{val}')
            else:
                logger.warning(f'overwrite:{overwrite},Can`t overwrite {key} data.')

    def _get(self, key: str):
        return self.data.get(key, None)

    def save(self, output: Optional[str] = None) -> None:
        save_path = output if output is not None else self.path

        with open(save_path, 'w') as f:
            f.write(json.dumps(self.data, indent=4, ensure_ascii=False))

        logger.info(f'Save Json File in: {save_path}.')

    def keys(self):
        return self.data.keys()

    def __call__(self, key: str):
        return self._get(key)

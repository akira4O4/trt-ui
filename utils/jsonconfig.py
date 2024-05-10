import os
import json
from typing import Optional
from loguru import logger


class JsonConfig:
    def __init__(self, path: Optional[str] = None) -> None:
        self._path = path
        self._data = {}
        if path is not None:
            self._load_json()

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

    def _load_json(self):
        base_name = os.path.basename(self.path)
        _, ext = os.path.splitext(base_name)
        if ext != '.json':
            logger.error('Input file is not json. ')
            exit()

        with open(self.path, 'r') as config_file:
            self.data = json.load(config_file)

    def reload(self, path: str) -> bool:
        if not os.path.exists(path):
            logger.error(f'Re-load json file: {path} is not found.')
            return False

        self._path = path
        self._load_json()

        return True

    def del_(self, key: str) -> bool:
        if self.data.get(key) is None:
            logger.error(f'Key: {key}is not found.')
            return False
        else:
            logger.info(f'Del {key}:{self.data[key]}.')
            del self.data[key]
            return True

    def add(self, kv: dict, overwrite: Optional[bool] = False) -> bool:
        for k, v in kv.items():
            self._add(k, v, overwrite)

    def _add(self, key: str, val, overwrite: Optional[bool] = False) -> bool:

        if self.data.get(key) is None or self.data.get(key) == "":
            self.data[key] = val
            logger.success(f'Set {key}:{val}')
            return True
        else:
            if overwrite:
                self.data[key] = val
                logger.success(f'Set {key}:{val}')
                return True
            else:
                return False

    def _get_val(self, key: str):
        return self.data.get(key, None)

    def save(self, output: Optional[str] = None) -> None:
        save_path = self.path

        if output is not None:
            save_path = output

        with open(save_path, 'w') as f:
            f.write(json.dumps(self.data, indent=4, ensure_ascii=False))

        logger.info(f'Save file in: {save_path}.')

    def keys(self):
        return self.data.keys()

    def __call__(self, key: str):
        return self._get_val(key)

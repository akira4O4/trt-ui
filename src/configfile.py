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

    def items(self):
        return self._data.items()

    def update(self, data: dict) -> None:
        self._data.update(data)

    def save(self, output: Optional[str] = None) -> None:
        save_path = output if output is not None else self.path

        with open(save_path, 'w') as f:
            f.write(json.dumps(self.data, indent=4, ensure_ascii=False))

        logger.info(f'Save Json File in: {save_path}.')

    def keys(self):
        return self.data.keys()

    def __str__(self) -> str:
        data_str = '\n'
        for k, v in self._data.items():
            data_str += f"{k} : {v}\n"
        return data_str

    def __call__(self, key: str):
        return self.data.get(key, None)

import os
from typing import Optional
from loguru import logger


class FilePath:
    def __init__(self, path: Optional[str] = None) -> None:
        self._path = path
        self._is_exists = False
        self._basename = ''
        self._dir = ''
        self._basename = ''
        self._name = ''
        self._suffix = ''
        if path is not None:
            self.decode()

    def decode(self) -> None:
        if os.path.isdir(self._path):
            self._dir = self._path
        else:
            self._dir, self._basename = os.path.split(self._path)
            self._name, self._suffix = os.path.splitext(self._basename)

        self._is_exists = os.path.exists(self._path)
        logger.info(f'Decode Path: {self.path}')

    @property
    def is_exists(self) -> bool:
        return self._is_exists

    @property
    def path(self) -> str:
        return self._path

    @path.setter
    def path(self, val: str) -> None:
        self._path = val

    @property
    def dir(self) -> str:
        return self._dir

    @dir.setter
    def dir(self, val: str) -> None:
        self._dir = val

    @property
    def basename(self) -> str:
        return self._basename

    @property
    def name(self) -> str:
        return self._name

    @property
    def suffix(self) -> str:
        return self._suffix

    def __repr__(self):
        return (
            f'Path:{self._path}\n'
            f'Dir: {self._dir}\n'
            f'Basename: {self._basename}\n'
            f'Name: {self._name}\n'
            f'Suffix: {self._suffix}'
        )


if __name__ == '__main__':
    fp = FilePath()
    fp.path = '/home/data/data/model.engine'
    fp.decode()
    print(fp)
    print(fp.is_exists)

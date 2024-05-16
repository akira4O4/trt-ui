from setuptools import setup, find_packages
from src.jsonfile import JsonFile


def get_install_requires() -> list:
    install_requires = [
        "pyqt5 >= 5.15.10"
        "loguru >= 0.7.2"
        "onnx >= 1.16.0"
        "onnxruntime >= 1.17.3"
        "setuptools >= 69.5.1"
    ]

    QT_VERSION = None

    try:
        import PyQt5  # NOQA
        QT_VERSION = "pyqt5"
    except ImportError:
        pass

    if QT_VERSION is None:
        try:
            import PyQt6  # NOQA
            QT_VERSION = "pyqt6"
        except ImportError:
            pass

    del QT_VERSION

    return install_requires


def get_description() -> str:
    description = 'This is an ONNX to TensorRT engine ui tool.'
    return description


VERSION = JsonFile('configs/version.json')


def main():
    setup(
        name=VERSION('app_name'),
        version=VERSION('version'),
        author=VERSION('author'),
        author_email=VERSION('e_mail'),
        license=VERSION('license'),
        description=get_description(),
        packages=find_packages(),
        install_requires=get_install_requires(),
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3 :: Only"
        ],
        package_data={
            "": ["configs/*.json", "doc/*.md", "icons/*"]

        },
        url=VERSION('github'),
        entry_points={
            "console_scripts": [
                "main=main:main",
            ],
        },
    )


if __name__ == '__main__':
    main()

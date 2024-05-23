from typing import List, Optional
from dataclasses import dataclass

import onnx
import onnxruntime
from loguru import logger


@dataclass
class ONNXIO:  # noqa
    name: str = ''
    type: str = ''
    shape: list = ''

    def __repr__(self):
        return f'Name: {self.name}\nType: {self.type}\nShape: {self.shape}'


class DeONNX:
    def __init__(self, onnx_path: Optional[str] = None):
        self._onnx_path = onnx_path
        self._output = None
        self._input = None
        self._node = None
        self._initializer = None
        self._graph = None
        self.onnx_session = None
        self._model = None
        self._inputs: List[ONNXIO] = []
        self._outputs: List[ONNXIO] = []

        self.num_of_input = 0
        self.num_of_output = 0

        self._is_dynamic = False

    def init(self):
        self._model = onnx.load(self._onnx_path)
        onnx.checker.check_model(self._model)
        self.onnx_session = onnxruntime.InferenceSession(self._onnx_path, providers=['CPUExecutionProvider'])

        self._graph: onnx.GraphProto = self._model.graph
        self._initializer = self._graph.initializer
        self._node = self._graph.node
        self._input = self._graph.input
        self._output = self._graph.output
        self.num_of_input = len(self._input)
        self.num_of_output = len(self._output)

        logger.info(f'Decode ONNX: {self._onnx_path}')
        self.decode_io()

    def set_onnx_path(self, path: str):
        self._onnx_path = path

    @property
    def is_dynamic(self) -> bool:
        return self._is_dynamic

    @property
    def inputs(self) -> List[ONNXIO]:
        return self._inputs

    @property
    def outputs(self) -> List[ONNXIO]:
        return self._outputs

    def get_input(self, idx: int) -> ONNXIO:
        return self._inputs[idx]

    def get_output(self, idx: int) -> ONNXIO:
        return self._outputs[idx]

    def decode_io(self) -> None:
        self._decode_input()
        self._decode_output()

    def _decode_input(self) -> None:
        inputs = self.onnx_session.get_inputs()
        self._inputs = []
        for item in inputs:
            self._inputs.append(
                ONNXIO(
                    item.name,
                    item.type,
                    item.shape
                )
            )
            if item.shape[0] is None:
                self._is_dynamic = True
        logger.info('Decode Input')

    def _decode_output(self) -> None:
        outputs = self.onnx_session.get_outputs()
        self._outputs = []
        for item in outputs:
            self._outputs.append(
                ONNXIO(
                    item.name,
                    item.type,
                    item.shape
                )
            )
        logger.info('Decode Output')

    def get_io_info(self) -> str:
        return self._get_inputs_info() + self._get_output_info()

    def _get_inputs_info(self) -> str:
        info = """Inputs:\n"""
        for item in self._inputs:
            info += f"\tname:\t{item.name}\n" \
                    f"\ttype:\t{item.type}\n" \
                    f"\tshape:\t{item.shape}\n\n"
        return info

    def _get_output_info(self) -> str:
        info = """Output:\n"""
        for item in self._outputs:
            info += f"\tname:\t{item.name}\n" \
                    f"\ttype:\t{item.type}\n" \
                    f"\tshape:\t{item.shape}\n\n"
        return info

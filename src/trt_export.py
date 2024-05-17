import os
import math
from typing import List, Optional, Union, Tuple
from loguru import logger

import tensorrt as trt
import common


class TRTExport:
    def __init__(
            self,
            onnx_path: str,
            output_path: str,
            fp32: Optional[bool] = True,
            fp16: Optional[bool] = False,
            is_dynamic: Optional[bool] = False,
            static_shape: List[int] = None,
            input_name: Optional[str] = '',
            dynamic_min_shape: Optional[List[int]] = None,
            dynamic_max_shape: Optional[List[int]] = None,
            workspace_size: Optional[int] = 1024
    ) -> None:
        self.onnx_path = onnx_path
        self.output_path = output_path

        if fp32 and fp16:
            logger.error(f'FP32:{fp32} and FP16:{fp16}')
            exit()
        if not fp32 and not fp16:
            logger.error(f'FP32:{fp32} and FP16:{fp16}')
            exit()

        self.fp32 = fp32
        self.fp16 = fp16

        self.is_dynamic = is_dynamic
        self._static_shape = static_shape
        self.input_name = input_name

        self.dynamic_min_shape = tuple(dynamic_min_shape)
        self.dynamic_max_shape = tuple(dynamic_max_shape)

        self.dynamic_mid_shape = dynamic_min_shape
        self.dynamic_mid_shape[0] = math.ceil(0.5 * (dynamic_min_shape[0] + dynamic_max_shape[0]))
        self.dynamic_mid_shape = tuple(self.dynamic_mid_shape)

        self.workspace_size = workspace_size
        self.engine = None
        self.builder = None
        self.network = None
        self.config = None
        self.runtime = None
        self.onnx_parser = None
        self.TRT_LOGGER = trt.Logger()

    def set_static_shape(self, shape: list) -> None:
        self._static_shape = shape

    @property
    def static_shape(self) -> list:
        return self._static_shape

    def init(self) -> None:
        self.builder = trt.Builder(self.TRT_LOGGER)
        self.network = self.builder.create_network(common.EXPLICIT_BATCH)
        self.config = self.builder.create_builder_config()
        self.runtime = trt.Runtime(self.TRT_LOGGER)
        self.onnx_parser = trt.OnnxParser(self.network, self.TRT_LOGGER)

        self.config.max_workspace_size = self.workspace_size
        self.builder.max_batch_size = self._static_shape[0]  # 推理的时候要保证batch_size<=max_batch_size

    def run(self) -> bool:
        try:
            if self.is_dynamic:
                profile = self.builder.create_optimization_profile()

                profile.set_shape(
                    self.input_name,
                    self.dynamic_min_shape,
                    self.dynamic_mid_shape,
                    self.dynamic_max_shape
                )

                self.config.add_optimization_profile(profile)

            else:
                self.network.get_input(0).shape = self.static_shape

            logger.info('Completed parsing the ONNX file')
            logger.info(f'Building an engine from file {self.onnx_path}; this may take a while...')
            # plan = builder.build_serialized_network(network,config)
            # engine = runtime.deserialize_cuda_engine(plan)
            self.engine = self.builder.build_engine(self.network, self.config)
            with open(self.output_path, 'wb') as f:
                # f.write(plan)
                f.write(self.engine.serialize())
            logger.success('Completed creating Engine')
            return True

        except:
            return False

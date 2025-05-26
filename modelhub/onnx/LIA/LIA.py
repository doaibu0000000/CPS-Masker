from pathlib import Path
from typing import List

import numpy as np
from xlib.file import SplittedFile
from xlib.image import ImageProcessor
from xlib.onnxruntime import (InferenceSession_with_device, ORTDeviceInfo,
                              get_available_devices_info)


class LIA:


    @staticmethod
    def get_available_devices() -> List[ORTDeviceInfo]:
        return get_available_devices_info()

    def __init__(self, device_info : ORTDeviceInfo):
        if device_info not in LIA.get_available_devices():
            raise Exception(f'device_info {device_info} is not in available devices for LIA')
        
        generator_path = Path(__file__).parent / 'generator.onnx'
        SplittedFile.merge(generator_path, delete_parts=False)
        if not generator_path.exists():
            raise FileNotFoundError(f'{generator_path} not found')
            
        self._generator = InferenceSession_with_device(str(generator_path), device_info)


    def get_input_size(self):

        return (256,256)

    def extract_motion(self, img : np.ndarray):

        feed_img = ImageProcessor(img).resize(self.get_input_size()).ch(3).swap_ch().to_ufloat32(as_tanh=True).get_image('NCHW')
        return self._generator.run(['out_drv_motion'], {'in_src': np.zeros((1,3,256,256), np.float32), 
                                                        'in_drv': feed_img, 
                                                        'in_drv_start_motion': np.zeros((1,20), np.float32),
                                                        'in_power' : np.zeros((1,), np.float32)
                                                        })[0]



    def generate(self, img_source : np.ndarray, img_driver : np.ndarray, driver_start_motion : np.ndarray, power):

        ip = ImageProcessor(img_source)
        dtype = ip.get_dtype()
        _,H,W,_ = ip.get_dims()

        out = self._generator.run(['out'], {'in_src': ip.resize(self.get_input_size()).ch(3).swap_ch().to_ufloat32(as_tanh=True).get_image('NCHW'),
                                            'in_drv' : ImageProcessor(img_driver).resize(self.get_input_size()).ch(3).swap_ch().to_ufloat32(as_tanh=True).get_image('NCHW'),
                                            'in_drv_start_motion' : driver_start_motion,
                                            'in_power' : np.array([power], np.float32)
                                            })[0].transpose(0,2,3,1)[0]

        out = ImageProcessor(out).to_dtype(dtype, from_tanh=True).resize((W,H)).swap_ch().get_image('HWC')
        return out


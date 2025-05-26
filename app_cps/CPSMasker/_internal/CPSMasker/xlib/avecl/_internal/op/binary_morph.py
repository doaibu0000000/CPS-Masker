from ..Tensor import Tensor
from .binary_dilate_circle import binary_dilate_circle
from .binary_erode_circle import binary_erode_circle
from .gaussian_blur import gaussian_blur
from .pad import pad
from .cast import cast

def binary_morph(input_t : Tensor, erode_dilate : int, blur : float, fade_to_border : bool = False, dtype=None) -> Tensor:

    x = input_t

    H,W = input_t.shape[-2:]

    x = pad(x, (...,(H,H),(W,W)), mode='constant', constant_value=0)

    if erode_dilate > 0:
        x = binary_erode_circle(x, radius=1, iterations=max(1,erode_dilate//2))
    elif erode_dilate < 0:
        x = binary_dilate_circle(x, radius=1, iterations=max(1,-erode_dilate//2) )

    if fade_to_border:
        h_clip_size = H + blur // 2
        w_clip_size = W + blur // 2
        x[...,:h_clip_size,:] = 0
        x[...,-h_clip_size:,:] = 0
        x[...,:,:w_clip_size] = 0
        x[...,:,-w_clip_size:] = 0

    if blur > 0:
        x = gaussian_blur(x, blur * 0.250, dtype=dtype)
    else:
        x = cast(x, dtype=dtype)

    return x[...,H:-H,W:-W]

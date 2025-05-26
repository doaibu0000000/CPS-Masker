from ..Tensor import Tensor

from .any_wise import any_wise

def cast(input_t : Tensor, dtype, output_t:Tensor=None) -> Tensor:

    return any_wise('O=I0', input_t, dtype=dtype, output_t=output_t)

from ..AShape import AShape
from ..AAxes import AAxes

class TransposeInfo:


    __slots__ = ['no_changes', 'o_shape']

    def __init__(self, shape : AShape, axes_order : AAxes):
        if shape.ndim != axes_order.ndim:
            raise ValueError('axes must match the shape')

        # Axes order changes nothing?
        self.o_shape = shape[axes_order]
        self.no_changes = axes_order == shape.axes_arange()




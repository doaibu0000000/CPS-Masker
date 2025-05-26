from ..AShape import AShape

class ReshapeInfo:


    __slots__ = ['o_shape']

    def __init__(self, shape, target_shape):
        o_shape = []

        remain_size = shape.size

        unk_axis = None
        for t_size in target_shape:
            t_size = int(t_size)
            if t_size != -1:
                mod = remain_size % t_size
                if mod != 0:
                    raise ValueError(f'Cannot reshape {shape} to {target_shape}.')
                remain_size /= t_size
            else:
                if unk_axis is not None:
                    raise ValueError('Can specify only one unknown dimension.')
                unk_axis = len(o_shape)
            o_shape.append( t_size )

        if unk_axis is not None:
            o_shape[unk_axis] = int(remain_size)
        self.o_shape = AShape(o_shape)
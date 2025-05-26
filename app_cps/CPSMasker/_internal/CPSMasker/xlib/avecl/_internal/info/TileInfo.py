import numpy as np
from ..AShape import AShape, AShape

class TileInfo:


    __slots__ = ['o_shape', 'axes_slices']

    def __init__(self, shape, tiles):
        if len(tiles) != shape.ndim:
            raise ValueError(f'tiles should match shape.ndim {shape.ndim}')

        self.o_shape = AShape(dim*tiles[i] for i,dim in enumerate(shape))

        c = [0]*shape.ndim

        axes_offsets = []
        for n in range(np.prod(tiles)):
            axes_offsets.append( c.copy() )
            for i in range(shape.ndim-1,-1,-1):
                c[i] += 1
                if c[i] < tiles[i]:
                    break
                c[i] = 0

        axes_slices = []
        for axes_offset in axes_offsets:
            sl = []
            for axis,tile in enumerate(axes_offset):
                axis_size = shape[axis]
                sl.append( slice(axis_size*tile, axis_size*(tile+1)) )
            axes_slices.append(tuple(sl))
        self.axes_slices = tuple(axes_slices)
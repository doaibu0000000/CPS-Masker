from typing import List

import numpy as np

from ..AShape import AShape
from ..AAxes import AAxes

class BroadcastInfo:


    __slots__ = ['o_shape', 'br_shapes', 'shapes_tiles', 'shapes_reduction_axes']

    def __init__(self, shapes : List[AShape]):

        highest_rank = sorted([shape.ndim for shape in shapes])[-1]

        br_shapes = [ (1,)*(highest_rank-shape.ndim) + shape for shape in shapes ]

        o_shape = AShape( np.max( [ [ br_shape.shape[axis] for br_shape in br_shapes] for axis in range(highest_rank) ], axis=1  ) )

        shapes_tiles = []
        shapes_reduction_axes = []
        for br_shape in br_shapes:
            shape_tile = []
            shape_reduction_axes = []
            for axis, (x,y) in enumerate(zip(br_shape.shape, o_shape.shape)):
                if x != y:
                    if x == 1 and y != 1:
                        shape_tile.append(y)
                        shape_reduction_axes.append(axis)
                    elif x != 1 and y == 1:
                        shape_tile.append(1)
                    else:
                        raise ValueError(f'operands could not be broadcast together with shapes {br_shape} {o_shape}')
                else:
                    shape_tile.append(1)

            shapes_tiles.append(shape_tile)
            shapes_reduction_axes.append( AAxes(shape_reduction_axes) )


        self.o_shape : AShape = AShape(o_shape)
        self.br_shapes : List[AShape] = br_shapes
        self.shapes_tiles : List[List] = shapes_tiles
        self.shapes_reduction_axes : List [AAxes] = shapes_reduction_axes


import math

import numpy as np

from ..AShape import AShape


class SliceInfo:
    __slots__ = ['o_shape', 'o_shape_kd', 'just_reshaped','axes_bes','axes_abs_bes']

    def __init__(self, shape : AShape, slices):

        new_slices = []
        before_ellipsis = None

        for s in slices:
            if s is Ellipsis:
                before_ellipsis = new_slices
                new_slices = []
                continue
            elif s is not None and not isinstance(s, (int,tuple) ):
                raise ValueError(f'unknown slice argument {s} of type {s.__class__}')

            new_slices.append(s)

        if before_ellipsis is not None:

            new_slices_n_axes = sum([ 1 for x in new_slices if x != None])
            before_ellipsis_n_axes = sum([ 1 for x in before_ellipsis if x != None])


            new_slices = before_ellipsis + \
                         [(None,None,None)]*max(0, shape.ndim-before_ellipsis_n_axes-new_slices_n_axes) + \
                         new_slices

        new_slices_n_axes = sum([ 1 for x in new_slices if x != None])
        if new_slices_n_axes > shape.ndim:
            raise ValueError('slices arguments more than shape axes')
        elif new_slices_n_axes < shape.ndim:

            new_slices += [(None,None,None)]*( shape.ndim - new_slices_n_axes )

        slices = tuple(new_slices)


        output_is_reshaped = True

        o_shape = []
        o_shape_kd = []
        axes_bes = []
        axes_abs_bes = []

        i_axis = 0


        for v in slices:
            if v is None:

                o_shape.append(1)
                continue

            i_axis_size = shape[i_axis]
            i_axis += 1

            if isinstance(v, int):
                if v < 0:
                    v += i_axis_size
                if v < 0 or v >= i_axis_size:
                    raise ValueError(f'index {v} is out of bounds for axis {i_axis} with size {i_axis_size}')
                b,e,s = v,v,0
            else:
                b,e,s = v
                if s == 0:
                    raise ValueError(f'slice step cannot be zero')

            # Fix begin, end, step values
            if s is None:
                s = 1
            if b is None:
                b = 0 if s >= 0 else i_axis_size-1
            if e is None:
                e = i_axis_size if s >= 0 else -1
            elif e < 0:
                e += i_axis_size
            if b < 0:
                b += i_axis_size

            if s >= 0:
                b = np.clip(b, 0, i_axis_size)
                e = np.clip(e, 0, i_axis_size)
                if b > e:
                    raise ValueError('for positive step, begin cannot be > end.')

                abs_b, abs_e, abs_s = b,e,s
            else:
                b = np.clip(b, 0, i_axis_size-1)
                e = np.clip(e, -1, i_axis_size)

                if b <= e:
                    raise ValueError('for negative step, begin cannot be <= end.')

                abs_s = -s
                abs_e = b + 1
                abs_b = b - (math.ceil( (b-e) / abs_s ) -1) * abs_s


            axes_bes.append( (b,e,s))
            axes_abs_bes.append( (abs_b, abs_e, abs_s))

            if i_axis_size != 1 and not (b == 0 and e == i_axis_size and s == 1):

                output_is_reshaped = False


            o_axis_size = max(0, math.ceil ( (e-b) / (s if s != 0 else 1) ) )

            if o_axis_size >= 1:

                o_shape.append(o_axis_size)



            o_shape_kd.append( max(1,o_axis_size) )

        self.just_reshaped = output_is_reshaped
        self.o_shape = AShape(o_shape)
        self.o_shape_kd = AShape(o_shape_kd)
        self.axes_bes = axes_bes
        self.axes_abs_bes = axes_abs_bes
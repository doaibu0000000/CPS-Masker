from ..Tensor import Tensor

class Initializer:

    def initialize_tensor(self, tensor : Tensor):

        raise NotImplementedError()

    def __str__(self): return 'Initializer'
    def __repr__(self): return self.__str__()

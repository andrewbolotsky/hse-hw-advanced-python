import numpy as np
from numpy.lib.mixins import NDArrayOperatorsMixin


class FileMixin:
    def save(self, filename):
        np.savetxt(filename, self._data, fmt="%.3f")

    @classmethod
    def load(cls, filename):
        data = np.loadtxt(filename)
        return cls(data)


class PrettyViewMixin:
    def __str__(self):
        return f"{self.__class__.__name__}({self._data})"

    def __repr__(self):
        return f"{self.__class__.__name__}({repr(self._data)})"


class GettersAndSettersMixin:
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = np.asarray(value)

    @property
    def shape(self):
        return self._data.shape

    @property
    def size(self):
        return self._data.size

    @property
    def dtype(self):
        return self._data.dtype


class ArrayWithFeatures(NDArrayOperatorsMixin, FileMixin, PrettyViewMixin, GettersAndSettersMixin):
    def __init__(self, data):
        self._data = np.asarray(data)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        out = kwargs.get('out', ())
        for x in inputs + out:
            if not isinstance(x, (np.ndarray, type(self))):
                return NotImplemented

        inputs = tuple(x._data if isinstance(x, type(self)) else x for x in inputs)
        if out:
            kwargs['out'] = tuple(x._data if isinstance(x, type(self)) else x for x in out)

        result = getattr(ufunc, method)(*inputs, **kwargs)

        if method == 'at':
            return None

        if type(result) is tuple:
            return tuple(type(self)(x) for x in result)
        elif method == 'reduce':
            return type(self)(result)
        else:
            return type(self)(result)
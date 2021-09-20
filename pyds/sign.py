from .is_a_number import *
from .is_a_tensor import *
from .is_a_numpy_array import *
from .is_a_pandas_series import *
from .is_a_pandas_dataframe import *


def sign(x):
    if isATensor(x):
        if isAPandasSeries(x) or isAPandasDataFrame(x):
            x = x.values.tolist()

        if isANumpyArray(x):
            x = x.tolist()

        return [sign(v) for v in x]

    else:
        assert isANumber(x), "`x` must be a number!"

        if x > 0:
            return 1
        if x < 0:
            return -1
        return 0

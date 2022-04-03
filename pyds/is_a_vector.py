from .is_iterable import *
from .is_a_numpy_array import *
from .is_a_pandas_series import *
from numpy import shape


def isAVector(x):
    if not isIterable(x):
        return False

    if isAPandasSeries(x):
        x = x.values

    try:
        return len(shape(x)) == 1

    except:
        return False

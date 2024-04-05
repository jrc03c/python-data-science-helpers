from numpy import shape

from .is_a_pandas_series import isAPandasSeries
from .is_iterable import isIterable


def isAVector(x):
    if not isIterable(x):
        return False

    if isAPandasSeries(x):
        x = x.values

    try:
        return len(shape(x)) == 1

    except:
        return False

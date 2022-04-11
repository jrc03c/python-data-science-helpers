from .is_a_function import *
from .is_a_numpy_array import *
from .is_a_pandas_dataframe import *
from .is_a_pandas_series import *
from .is_a_tensor import *


def find(a, b):
    if isAFunction(a):
        fn = a
        x = b

    else:
        fn = b
        x = a

    assert isAFunction(
        fn
    ), "You must pass a function and a tensor into the `find` function!"

    assert isATensor(
        x
    ), "You must pass a function and a tensor into the `find` function!"

    if isAPandasDataFrame(x) or isAPandasSeries(x):
        x = x.values

    if isANumpyArray(x):
        x = x.tolist()

    for item in x:
        try:
            if fn(item):
                return item

        except:
            pass

    for item in x:
        try:
            result = find(fn, item)

            if result is not None:
                return result

        except:
            pass

    return None

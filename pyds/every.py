from .is_a_function import isAFunction
from .is_a_numpy_array import isANumpyArray
from .is_a_pandas_dataframe import isAPandasDataFrame
from .is_a_pandas_series import isAPandasSeries
from .is_a_tensor import isATensor


def every(a, b):
    if isAFunction(a):
        x = b
        fn = a

    else:
        x = a
        fn = b

    assert isATensor(
        x
    ), "You must pass a function and a tensor into the `every` function!"

    assert isAFunction(
        fn
    ), "You must pass a function and a tensor into the `every` function!"

    if isAPandasDataFrame(x) or isAPandasSeries(x):
        x = x.values

    if isANumpyArray(x):
        x = x.tolist()

    for value in x:
        if not fn(value):
            return False

    return True

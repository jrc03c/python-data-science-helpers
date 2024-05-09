from numpy import array

from .is_a_function import is_a_function
from .is_a_numpy_array import is_a_numpy_array
from .is_a_pandas_dataframe import is_a_pandas_dataframe
from .is_a_pandas_series import is_a_pandas_series
from .is_a_tensor import is_a_tensor
from .is_jagged import is_jagged
from .set import set

old_map = map


def map(a, b):
    if is_a_function(a):
        fn = a
        arr = b
    else:
        fn = b
        arr = a

    assert is_a_function(
        fn
    ), "You must pass a function and a tensor into the `map` function!"

    assert is_a_tensor(
        arr
    ), "You must pass a function and a tensor into the `map` function!"

    if is_a_pandas_series(arr) or is_a_pandas_dataframe(arr):
        arr = arr.values.tolist()

    if is_a_numpy_array(arr):
        arr = arr.tolist()

    out = list(old_map(fn, arr))
    types = set(list(old_map(lambda v: type(v), out)))

    if is_jagged(out) or len(types) > 1:
        return array(out, dtype=object)

    else:
        return array(out)

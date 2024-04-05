import unittest

from numpy import array, ndarray
from numpy.random import normal, random
from pandas import DataFrame as DF

from pyds import isANumpyArray


class IsANumpyArrayTestCase(unittest.TestCase):
    def test(self):
        arrays = [
            normal(size=100),
            random(size=[2, 3, 4, 5]),
            array([2, 3, 4, 5]),
            ndarray([2, 3, 4, 5]),
        ]

        for arr in arrays:
            self.assertTrue(isANumpyArray(arr), msg="Failed to identify numpy arrays!")

        others = [
            234,
            True,
            False,
            "foo",
            lambda x: x * 2,
            {"hello": "world"},
            [2, 3, 4, 5],
            DF(normal(size=[100, 100])),
        ]

        for item in others:
            self.assertFalse(
                isANumpyArray(item), msg="Failed to identify non-numpy-arrays!"
            )

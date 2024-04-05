import unittest

from numpy.random import normal
from pandas import DataFrame, Series

from pyds import isAPandasDataFrame


class IsAPandasDataFrameTestCase(unittest.TestCase):
    def test(self):
        dfs = [
            DataFrame(normal(size=[100, 100])),
            DataFrame(),
        ]

        for df in dfs:
            self.assertTrue(
                isAPandasDataFrame(df), msg="Failed to identify pandas DataFrames!"
            )

        others = [
            Series(normal(size=100)),
            [[2, 3, 4], [5, 6, 7]],
            234,
            True,
            False,
            None,
            lambda x: x * 2,
            {"hello", "world"},
            "foo",
        ]

        for item in others:
            self.assertFalse(
                isAPandasDataFrame(item),
                msg="Failed to identify non-pandas-DataFrames!",
            )

from pandas.core.series import Series
import pytest
from mbdiff.diff_query import DiffQuery


def test_diff_query_basic_1(df_basic):
    query = DiffQuery('ints', '=', 1)
    res_df = query.apply(df_basic)
    assert len(res_df.index) == 1

def test_diff_query_basic_2(df_basic):
    query = DiffQuery('ints', '>', 1)
    res_df = query.apply(df_basic)
    assert len(res_df.index) == 8

def test_diff_query_raise():
    with pytest.raises(ValueError):
        DiffQuery('ints', '==', 1)

def test_mark_groups(df_basic):
    query = DiffQuery('ints', '=', 1)
    query.mark_groups(df_basic)
    exp = Series(['inlier', 'outlier'] + ['inlier'] * 8)
    assert all(df_basic['outlier'] == exp)

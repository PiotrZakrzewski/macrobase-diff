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

def test_diff_query_raise(df_basic):
    with pytest.raises(ValueError):
        DiffQuery('ints', '==', 1)

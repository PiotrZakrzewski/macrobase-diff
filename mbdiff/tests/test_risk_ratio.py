from mbdiff.risk_ratio import calc_support
import pytest
from pandas import DataFrame, Series

FIXTURE_DF_LEN = 10

@pytest.fixture
def int_column():
    return Series([x for x in range(FIXTURE_DF_LEN)])

@pytest.fixture
def float_column():
    return Series([x*1.1 for x in range(FIXTURE_DF_LEN)])

@pytest.fixture
def cat_col_all_same():
    return Series(["cat1" for _ in range(FIXTURE_DF_LEN)])

@pytest.fixture
def outlier_col():
    return Series(["inlier" for _ in range(FIXTURE_DF_LEN)])

@pytest.fixture
def df_basic(int_column, float_column, cat_col_all_same, outlier_col):
    return DataFrame({
        'ints': int_column,
        'floats':float_column,
        'cats': cat_col_all_same,
        'outlier': outlier_col,
    })

def test_risk_basic():
    pass

def test_support(df_basic):
    assert calc_support(df_basic, 'cats', 'cat1') == pytest.approx(1.0)
    assert calc_support(df_basic, 'cats', 'cat2') == pytest.approx(0.0)
    assert calc_support(df_basic, 'ints', 1) == pytest.approx(0.1)

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

@pytest.fixture
def df_attr_basic():
    return DataFrame({
        'attr1': ['a', 'b'],
        'attr2': ['a', 'b'],
    })

@pytest.fixture
def df_outliers(int_column, float_column, cat_col_all_same, outlier_col):
    outlier_col[9] = "outlier"
    float_column[9] = 999.8
    cat_col_all_same[9] = "cat2" 
    return DataFrame({
        'ints': int_column,
        'floats':float_column,
        'cats': cat_col_all_same,
        'outlier': outlier_col,
    })

@pytest.fixture
def df_outliers_balanced(int_column, float_column, cat_col_all_same, outlier_col):
    outlier_col[9] = "outlier"
    outlier_col[8] = "outlier"
    float_column[9] = 999.7
    float_column[8] = 999.8
    cat_col_all_same[9] = "cat2" 
    cat_col_all_same[8] = "cat1" 
    cat_col_all_same[7] = "cat2" 
    return DataFrame({
        'ints': int_column,
        'floats':float_column,
        'cats': cat_col_all_same,
        'outlier': outlier_col,
    })

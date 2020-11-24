from mbdiff.risk_ratio import calc_support, risk_ratio
import pytest
from numpy import nan


def test_risk_basic_null_1(df_outliers):
    """Due to lack of cat2 in the inliers the result will be NaN."""
    comb = {"cats": "cat2"}
    assert risk_ratio(comb, df_outliers) is nan


def test_risk_basic_null_2(df_outliers):
    """Due to lack of cat1 in the outliers the result will be 0.0."""
    comb = {"cats": "cat1"}
    assert risk_ratio(comb, df_outliers) == pytest.approx(0.0)


def test_risk_basic_balanced(df_outliers_balanced):
    """Due to lack of cat1 in the outliers the result will be 0.0."""
    comb = {"cats": "cat2"}
    assert risk_ratio(comb, df_outliers_balanced) == pytest.approx(4.0)
    comb = {"cats": "cat1"}
    assert risk_ratio(comb, df_outliers_balanced) == pytest.approx(0.25)


def test_support(df_basic):
    assert calc_support(df_basic, "cats", "cat1") == pytest.approx(1.0)
    assert calc_support(df_basic, "cats", "cat2") == pytest.approx(0.0)
    assert calc_support(df_basic, "ints", 1) == pytest.approx(0.1)

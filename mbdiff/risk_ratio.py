from pandas import DataFrame


def calc_support(df, column, value) -> float:
    """Calculate number of rows containing given value for given column."""
    supp = df[df[column] == value]
    return len(supp.index) / len(df.index)


def risk_ratio(attr_combination: dict, df) -> float:
    """Calculate risk ratio between two sets of attributes."""
    outliers = df[df["outlier"] == "outlier"]
    inliers = df[df["outlier"] == "inlier"]
    out_with_attr = filter_on_attrs(outliers, attr_combination)
    in_with_attr = filter_on_attrs(inliers, attr_combination)
    a0 = len(out_with_attr.index)
    ai = len(in_with_attr.index)
    b0 = len(outliers.index) - a0
    bi = len(inliers.index) - ai
    top_d = a0 + ai
    denom_d = b0 + bi
    if top_d == 0 or denom_d == 0:
        return 0
    top = a0 / top_d
    denom = b0 / denom_d
    if denom < 0.01:
        return 0.0
    return top / denom


def filter_on_attrs(df, attrs: dict) -> DataFrame:
    for column, value in attrs.items():
        df = df[df[column] == value]
    return df

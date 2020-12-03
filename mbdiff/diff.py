from typing import List
from pandas import DataFrame, read_csv
from mbdiff.diff_query import DiffQuery, InvalidQuery
from mbdiff.risk_ratio import risk_ratio
from numpy import nan
from mbdiff.apriori import explain as aprio_explain


def diff_file(
    path_to_df: str,
    query: DiffQuery,
    max_order: int,
    min_risk: float,
    min_support: float,
):
    """Given a tab delimited file and a distinguishing metric return explanations."""
    df = read_csv(path_to_df)
    if query.column not in df.columns:
        raise InvalidQuery("Query column is not present in the data")
    print("Outliers:")
    print(query.apply(df).to_string())
    return diff(df, query, max_order, min_risk, min_support)


def diff(
    df: DataFrame, query: DiffQuery, max_order: int, min_risk: float, min_support: float
):
    """Return explanations, invalid and below support criterium attribute combinations."""
    query.mark_groups(df)
    ignored_cols = []
    # ignore all non categorical columns
    for i, column in enumerate(df.columns):
        if df.dtypes[i] != "object":
            ignored_cols.append(column)
    sel_cols = [col for col in df.columns if col not in ignored_cols]
    df = df[sel_cols]
    return _apriori_diff(df, max_order, min_support, min_risk)


def _apriori_diff(df: DataFrame, max_order: int, min_support: float, min_risk: float):
    """Explanation mining from attributes close to macrobase DIFF, with use of Apriori."""
    explanations = aprio_explain(df, min_support, max_order)
    results, invalid = [], []
    for explanation in explanations:
        rr = risk_ratio(explanation, df)
        res = (rr, explanation)
        if rr is nan or rr <= min_risk:
            invalid.append(explanation)
        else:
            results.append(res)
    return results, invalid

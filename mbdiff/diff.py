from pandas import DataFrame, read_csv
from mbdiff.diff_query import DiffQuery
from mbdiff.risk_ratio import risk_ratio
from mbdiff.attribute_mining import get_combs


def diff_file(
    path_to_df: str,
    query: DiffQuery,
    max_order: int,
    min_risk: float,
    min_support: float,
) -> list:
    """Given a tab delimited file and a distinguishing metric return explanations."""
    df = read_csv(path_to_df)
    print("Outliers:")
    print(query.apply(df).to_string())
    return diff(df, query, max_order, min_risk, min_support)


def diff(
    df: DataFrame, query: DiffQuery, max_order: int, min_risk: float, min_support: float
) -> list:
    query.mark_groups(df)
    ignored_cols = ["outlier"]
    # ignore all non categorical columns
    for i, column in enumerate(df.columns):
        if df.dtypes[i] != "object":
            ignored_cols.append(column)
    combinations = get_combs(df, max_order, min_support, ignored_cols)
    results = []
    for combination in combinations:
        rr = risk_ratio(combination, df)
        if rr >= min_risk:
            results.append((rr, combination))
    return results

from typing import Tuple
from pandas import DataFrame
from mbdiff.diff_query import DiffQuery

def diff_file(path_to_df: str, query:DiffQuery, max_order:int, min_risk:float, min_support:float) -> Tuple:
    """Given a tab delimited file and a distinguishing metric return explanations."""
    df = DataFrame(path_to_df)
    return diff(df, query, max_order, min_risk, min_support)

def diff(df: DataFrame, query:DiffQuery, max_order:int, min_risk:float, min_support:float) -> Tuple:
    query.apply(df)

from typing import Tuple
from pandas import DataFrame

def diff_file(path_to_df: str, metric:str, max_order:int, min_risk:float, min_support:float) -> Tuple:
    """Given a tab delimited file and a distinguishing metric return explanations."""
    df = DataFrame(path_to_df)
    return diff(df, metric, max_order, min_risk, min_support)

def diff(df: DataFrame, metric:str, max_order:int, min_risk:float, min_support:float) -> Tuple:
    pass

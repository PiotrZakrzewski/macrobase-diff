"""Present explanations in a more approachable way."""
from typing import List
from tabulate import tabulate
from pandas import DataFrame


def present_explanations(explanations: List) -> str:
    pres_df = []
    for score, explanation in explanations:
        row = {"score": score}
        row = {**row, **explanation}
        pres_df.append(row)
    pres_df = DataFrame(pres_df)
    # NaN means "any value", represent as "-" just like in the original paper
    pres_df.fillna("-", inplace=True)
    return tabulate(pres_df, headers="keys")

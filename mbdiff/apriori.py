from efficient_apriori import apriori
import numpy as np

def df_to_apriori(df):
    """Convert pandas df to a data structure understood by efficient apriori."""
    [tuple(row) for row in df.values.tolist()]
    res = []
    for _, row in df.iterrows():
        transation = []
        for col in df.columns:
            val = row[col]
            if val is np.nan:
                continue
            attr_record = f"{col}:{val}"
            transation.append(attr_record)
        res.append(tuple(transation))
    return res


def format_res(apriori_results):
    """Convert apriori results to what Mb Diff expects."""
    explanations = [rule.lhs for rule in apriori_results]
    dict_form_explanations = []
    for explanation in explanations:
        d = {}
        for term in explanation:
            col, value = term.split(":")
            d[col] = value
        dict_form_explanations.append(d)
    return dict_form_explanations


def explain(df, min_support, max_order):
    data = df_to_apriori(df)
    _, rules = apriori(data, min_support, max_length=max_order)
    outlier_explanations = [r for r in rules if "outlier:outlier" in r.rhs]
    return format_res(outlier_explanations)

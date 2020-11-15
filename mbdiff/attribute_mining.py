from pandas.core.frame import DataFrame
from mbdiff.risk_ratio import calc_support
from collections import defaultdict
from itertools import permutations
from pandas import DataFrame


def get_combs(
    df: DataFrame, max_order: int, min_support: float, ignore: list = []
) -> list:
    val_base = defaultdict(list)
    for column in df.columns:
        if column in ignore:
            continue
        values = set(df[column])
        for value in values:
            if calc_support(df, column, value) >= min_support:
                val_base[column].append(value)
    single_attrs = []
    for column in val_base:
        for val in val_base[column]:
            t = ((column, val),)
            single_attrs.append(t)

    def recurse(order, current):
        if order == 0:
            return current
        if not current:
            return recurse(order - 1, single_attrs)
        current_plus_one = []
        for entry in current:
            for single_attr in single_attrs:
                extended_entry = entry + single_attr
                current_plus_one.append(extended_entry)
        return recurse(order - 1, current_plus_one)

    combs = recurse(max_order, [])
    combs = prune(combs)
    dicted = []
    for comb in combs:
        dicted_comb = {key: value for key, value in comb}
        dicted.append(dicted_comb)
    return dicted


def prune(attr_combs):
    pruned = []
    for comb in attr_combs:
        no_dupes = {key: value for key, value in comb}
        t = [(key, value) for key, value in no_dupes.items()]
        t = sorted(t, key=lambda x: (x[0], x[1]))
        t = tuple(t)
        if not t in pruned:
            pruned.append(t)
    return pruned

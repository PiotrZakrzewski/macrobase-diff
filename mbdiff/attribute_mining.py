from mbdiff.risk_ratio import calc_support

def get_combs(df, max_order, min_support):
    combs = []
    for column in df.columns:
        if column == 'outlier':
            continue
        values = set(df[column])
        for value in values:
            comb = {column: value}
            if calc_support(df, column, value) >= min_support:
                combs.append(comb)
    for _ in range(max_order - 1):
        combs_higher = []
        checked = set()
        for comb1 in combs:
            for comb2 in combs:
                if comb1 == comb2:
                    continue
                h = _dict_hash(comb1), _dict_hash(comb2)
                if h in checked:
                    continue
                checked.add(h)
                rev_h = h[1], h[0]
                checked.add(rev_h)
                comb = {**comb1, **comb2}
                if len(comb.keys()) > len(comb1.keys()):
                    combs_higher.append(comb)
        combs = combs_higher
    return combs


def _dict_hash(d):
    return hash(tuple(sorted(d.items())))

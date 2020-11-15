from mbdiff.attribute_mining import get_combs

def test_get_combs_basic(df_basic):
    combs = get_combs(df_basic, 1, 0.2, ["outlier"])
    assert combs == [{'cats': 'cat1'}]

def test_get_combs_2_order(df_attr_basic):
    combs = get_combs(df_attr_basic, 2, 0.0, ["outlier"])
    expected = [
        {'attr1': 'a'},
        {'attr1': 'b'},
        {'attr1': 'a', 'attr2': 'a'},
        {'attr1': 'a', 'attr2': 'b'},
        {'attr1': 'b', 'attr2': 'a'},
        {'attr1': 'b', 'attr2': 'b'},
        {'attr2': 'a'},
        {'attr2': 'b'},
        ]
    assert combs == expected

from funcs.funcs_03 import fact


def test_fact_0():
    result = fact(0)
    assert result == 1


def test_fact_more_0():
    result = fact(5)
    assert result == 120

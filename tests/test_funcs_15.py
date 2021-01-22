from funcs.funcs_15 import func2


def test_factorial():
    numbers = [1, 8]
    result = func2(numbers)
    assert result == {1: 1, 8: 384}

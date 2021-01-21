from funcs.funcs_05 import sum_args


def test_sum_args():
    args = [1, 2, 3, 4, 5, 6]
    result = sum_args(*args)
    assert result == 70

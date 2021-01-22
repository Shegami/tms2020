from funcs.funcs_17 import fact, sin1
import math


def test_fact():
    result = fact(12)
    assert result == 479001600


def test_sin():
    result = sin1(math.pi/6, 0.01)
    assert result == 0.39793018543425074

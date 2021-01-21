from funcs.funcs_01 import hello_name


def test_names():
    result = hello_name('Igor')
    assert result == 'Hello, Igor'

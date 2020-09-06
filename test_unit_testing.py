import pytest


@pytest.mark.parametrize("param1, param2,param3,expected", [
    ([0, 0], [1, 1], 5, 5),
    ([0, 1], [1, 0], 2, -1),
    ])
def test_linearest(param1, param2, param3, expected):
    from func_linearest import linearest
    answer = linearest(param1, param2, param3)
    assert answer == expected

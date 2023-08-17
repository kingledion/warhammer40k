from rules.util import *

def test_parse_variable():

    assert_parse_variable('d3', (1, 'd3', 0))
    assert_parse_variable('d6+2', (1, 'd6', 2))
    assert_parse_variable('2d3+1', (2, 'd3', 1))
    assert_parse_variable('6d6', (6, 'd6', 0))

    print("Test parse_variable passed!")


def assert_parse_variable(arg, exp):
    got = parse_variable(arg)
    assert got == exp , f'Expected {exp}; got {got}'
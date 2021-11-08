import pytest
from aoc import day_07

def test_part1():
    data = ['123 -> x',
            '456 -> y',
            'x AND y -> d',
            'x OR y -> e',
            'x LSHIFT 2 -> f',
            'y RSHIFT 2 -> g',
            'NOT x -> h',
            'NOT y -> i']
    assert day_07.part1(data, 'd') == 72
    assert day_07.part1(data, 'e') == 507
    assert day_07.part1(data, 'f') == 492
    assert day_07.part1(data, 'g') == 114
    assert day_07.part1(data, 'h') == 65412
    assert day_07.part1(data, 'i') == 65079
    assert day_07.part1(data, 'x') == 123
    assert day_07.part1(data, 'y') == 456

def test_part2():
    assert day_07.part2([]) == 0


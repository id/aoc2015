import pytest
from aoc import day_02

def test_part1():
    assert 58 == day_02.part1([[2,3,4]]);
    assert 43 == day_02.part1([[1,1,10]]);

def test_part2():
    assert 34 == day_02.part2([[2,3,4]]);
    assert 14 == day_02.part2([[1,1,10]]);

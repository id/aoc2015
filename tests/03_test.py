import pytest
from aoc import day_03

def test_part1():
    assert 2 == day_03.part1('>');
    assert 4 == day_03.part1('^>v<');
    assert 2 == day_03.part1('^v^v^v^v^v');

def test_part2():
    assert 3 == day_03.part2('^v');
    assert 3 == day_03.part2('^>v<');
    assert 11 == day_03.part2('^v^v^v^v^v');

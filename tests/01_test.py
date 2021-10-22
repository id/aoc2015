import pytest
from aoc import day_01

def test_part1():
    assert 0 == day_01.part1('(())');
    assert 0 == day_01.part1('()()');
    assert 3 == day_01.part1('(((');
    assert 3 == day_01.part1('(()(()(');
    assert 3 == day_01.part1('))(((((');
    assert -1 == day_01.part1('())');
    assert -1 == day_01.part1('))(');
    assert -3 == day_01.part1(')))');
    assert -3 == day_01.part1(')())())');

def test_part2():
    assert 1 == day_01.part2(')');
    assert 5 == day_01.part2('()())');

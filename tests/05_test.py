import pytest
from aoc import day_05

def test_part1():
    assert day_05.is_nice('ugknbfddgicrmopn')
    assert day_05.is_nice('aaa')
    assert not day_05.is_nice('jchzalrnumimnmhp')
    assert not day_05.is_nice('haegwjzuvuyypxyu')
    assert not day_05.is_nice('dvszwmarrgswjxmb')

def test_part2():
    assert not day_05.has_pair_of_two('aaa')
    assert day_05.is_nice_v2('qjhvhtzxzqqjkmpb')
    assert day_05.has_pair_of_two('qjhvhtzxzqqjkmpb')
    assert day_05.one_letter_repeats('qjhvhtzxzqqjkmpb')
    assert day_05.is_nice_v2('xxyxx')
    assert day_05.has_pair_of_two('xxyxx')
    assert day_05.one_letter_repeats('xxyxx')
    assert not day_05.is_nice_v2('uurcxstgmygtbstg')
    assert day_05.has_pair_of_two('uurcxstgmygtbstg')
    assert not day_05.one_letter_repeats('uurcxstgmygtbstg')
    assert not day_05.is_nice_v2('ieodomkazucvgmuy')
    assert not day_05.has_pair_of_two('ieodomkazucvgmuy')
    assert day_05.one_letter_repeats('ieodomkazucvgmuy')

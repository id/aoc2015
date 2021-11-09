import pytest
from aoc import day_08

@pytest.fixture
def line1():
    return '""'

@pytest.fixture
def line2():
    return '"abc"'

@pytest.fixture
def line3():
    return r'"aaa\"aaa"'

@pytest.fixture
def line4():
    return r'"\x27"'

def test_parse_line(line1, line2, line3, line4):
    assert day_08.parse_line(line1) == 0
    assert day_08.parse_line(line2) == 3
    assert day_08.parse_line(line3) == 7
    assert day_08.parse_line(line4) == 1

def test_parse_line2(line1, line2, line3, line4):
    assert day_08.parse_line2(line1) == 6
    assert day_08.parse_line2(line2) == 9
    assert day_08.parse_line2(line3) == 16
    assert day_08.parse_line2(line4) == 11

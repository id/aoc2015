import pytest
import operator
from aoc import day_06

@pytest.fixture
def line1():
    return 'turn on 0,0 through 999,999'

@pytest.fixture
def line2():
    return 'toggle 0,0 through 999,0'

@pytest.fixture
def line3():
    return 'turn off 499,499 through 500,500'

@pytest.fixture
def line4():
    return 'turn on 499,499 through 500,500'

@pytest.fixture
def line5():
    return 'turn on 0,0 through 0,0'

@pytest.fixture
def line6():
    return 'toggle 461,550 through 564,900'

@pytest.fixture
def line7():
    return 'turn off 370,39 through 425,839'

@pytest.fixture
def line8():
    return 'turn off 464,858 through 833,915'

def test_parse_line(line1, line2, line3):
    assert day_06.parse_line(line1) == (1, (0,0), (999,999))
    assert day_06.parse_line(line2) == (2, (0,0), (999,0))
    assert day_06.parse_line(line3) == (-1, (499,499), (500,500))

def test_part1(line1, line2, line3, line4, line5):
    assert day_06.part1([day_06.parse_line(line1)]) == 1000000
    assert day_06.part1([day_06.parse_line(line2)]) == 1000
    assert day_06.part1([day_06.parse_line(line1),
                         day_06.parse_line(line2)]) == (1000000-1000)
    assert day_06.part1([day_06.parse_line(line1),
                         day_06.parse_line(line3)]) == (1000000-4)
    assert day_06.part1([day_06.parse_line(line4)]) == 4
    assert day_06.part1([day_06.parse_line(line4),
                         day_06.parse_line(line3)]) == 0
    assert day_06.part1([day_06.parse_line(line4),
                         day_06.parse_line(line2)]) == 1004
    assert day_06.part1([day_06.parse_line(line1),
                         day_06.parse_line(line3),
                         day_06.parse_line(line4)]) == 1000000
    assert day_06.part1([day_06.parse_line(line5)]) == 1


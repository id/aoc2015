import pytest
from aoc import day_09

def test_parse_line():
    assert day_09.parse_line('London to Dublin = 464') == ('London', 'Dublin', 464)

def test_part1():
    edges = [('London', 'Dublin', 464), ('London', 'Belfast', 518), ('Dublin', 'Belfast', 141)]
    assert day_09.part1(edges) == 605

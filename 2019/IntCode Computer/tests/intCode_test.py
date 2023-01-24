import sys
sys.path.append("../IntCode Computer")
from day02 import day02, day02_p
from day05 import day05, day05_p

def test_second_day():
    assert day02.day02()        == 6087827, "day02 failed"

def test_second_day_plus():
    assert day02_p.day02_plus() == 5379, "day02+ failed"

def test_fifth_day():
    assert day05.day05()        == 5074395, "day05 failed"

def test_fifth_day_plus_ex_0():
    assert day05_p.day05_plus(0, "./day05/input_p.txt")  == 999

def test_fifth_day_plus_ex_8():
    assert day05_p.day05_plus(8, "./day05/input_p.txt")  == 1000

def test_fifth_day_plus_ex_10():
    assert day05_p.day05_plus(10, "./day05/input_p.txt") == 1001

def test_fifth_day_plus():
    assert day05_p.day05_plus(0) == 999

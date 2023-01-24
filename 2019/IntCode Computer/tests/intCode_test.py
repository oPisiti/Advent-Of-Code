import sys
sys.path.append("../IntCode Computer")
from day02 import day02, day02_p
from day05 import day05

def test_second_day():
    assert day02.day02()        == 6087827, "day02 failed"

def test_second_day_plus():
    assert day02_p.day02_plus() == 5379, "day02+ failed"

def test_fifth_day():
    assert day05.day05()        == 5074395, "day05 failed"
import sys
sys.path.append("../IntCode Computer")
from day02 import day02, day02_p
from day05 import day05, day05_p
from day09 import day09

def test_second_day():
    assert day02.day02()        == 6087827, "day02 failed"

def test_second_day_plus():
    assert day02_p.day02_plus() == 5379, "day02+ failed"

def test_fifth_day():
    assert day05.day05()        == 5074395, "day05 failed"

def test_fifth_day_plus_ex_0():
    assert day05_p.day05_plus(0, "./day05/input_p_ex.txt")  == 999

def test_fifth_day_plus_ex_8():
    assert day05_p.day05_plus(8, "./day05/input_p_ex.txt") == 1000

def test_fifth_day_plus_ex_10():
    assert day05_p.day05_plus(10, "./day05/input_p_ex.txt") == 1001

def test_fifth_day_plus():
    assert day05_p.day05_plus(5) == 8346937

def test_ninth_day_ex():
    assert day09.day09(0, "./day09/input_ex.txt") == 99

def test_ninth_day():
    assert day09.day09(1) == 3013554615

def test_ninth_day_plus():
    assert day09.day09(2) == 50158
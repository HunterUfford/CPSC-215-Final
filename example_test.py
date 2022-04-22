import pytest

def calc(num1, num2):
    
    return num1 + num2

def test_calc():
    assert (0.1 + 0.2) == pytest.approx(0.3) # Approximates a number for floating point comparisons
    #pytest.fail("Fails") # fails a test when called
    #pytest.exit("Exit") # exits from all future tests
    #pytest.skip() # Skips the current test
    assert calc(1,2) == 3, "assert failed"

def test_calc2():
    assert calc(-1,2) == 1, "assert failed"
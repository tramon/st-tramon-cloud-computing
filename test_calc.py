import pytest

from calc.calculations import sum_calculation, tricky_divide


def test_sum():
    assert sum_calculation(2, 3) == 5


#@pytest.mark.skipif(reason="known defect")
def test_tricky_divide():
    assert tricky_divide(12, 6) == 2

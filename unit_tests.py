import pytest
from app import sum_calculation, tricky_divide


def test_sum():
    assert sum_calculation(2, 3) == 5


def test_tricky_divide():
    assert tricky_divide(6, 2) == 3

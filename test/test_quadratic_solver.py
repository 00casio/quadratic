import pytest
from src import solve

def test_no_real_roots():
    assert solve(1, 0, 1) == "No real roots"

def test_one_real_root():
    assert solve(1, 2, 1) == -1.0

def test_two_real_roots():
    roots = solve(1, -3, 2)
    assert roots == (2.0, 1.0) or roots == (1.0, 2.0)

def test_invalid_coefficient_a():
    with pytest.raises(ValueError):
        solve(0, 2, 1)

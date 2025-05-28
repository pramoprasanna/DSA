from Patterns.Two_Pointers.Solution.Day06_Move_Zeros import move_zeros
import pytest


@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]),
    ([1, 0, 3, 0], [(1, 3, 0, 0)]),
    ([0, 2, 3], [2, 3, 0]),
    ([], []),
    ([0], [0]),
    ([0, 1, 0, 0], [1, 0, 0, 0])
])
def test_move_zeros(nums, expected):
    assert (move_zeros(nums)) == expected

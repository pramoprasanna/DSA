import pytest
from Patterns.Two_Pointers.Solution.Day02_MatchSumFromArray import matsum_fromarray, matsum_fromarray_allmatches


@pytest.mark.parametrize("nums, target, expected", [
    ([1, 2, 3, 4, 5, 6], 7, [(1, 6), (2, 5), (3, 4)]),
    ([1, 2, 3, 9], 10, [(1, 4)]),
    ([1, 2, 3], 10, []),
    ([], 5, []),
    ([5], 5, [])
])
def test_matsumfromarray_allmatches(nums, target, expected):
    assert matsum_fromarray_allmatches(nums, target) == expected


@pytest.mark.parametrize("nums, target, expected", [
    ([1, 2, 3, 4, 5, 6], 7, (1, 6)),
    ([1, 2, 3, 9], 10, (1, 4)),
    ([1, 2, 3], 10, "No match"),
    ([], 5, "No match"),
    ([5], 5, "No match")
])
def test_matsumfromarray(nums, target, expected):
    assert matsum_fromarray(nums, target) == expected

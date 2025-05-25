import pytest
from Patterns.Two_Pointers.Solution.Day03_DuplicateRemovalFromArrayInt_RECOMMENDED import remove_duplicates


@pytest.mark.parametrize("nums, expected", [
    ([1, 1, 3, 3, 4, 4], 3),
    ([1, 2, 3, 4], 4),
    ([1, 1, 1], 1),
    ([], 0)
])
def test_duplicateremoval(nums, expected):
    nums_copy = nums[:]
    result = remove_duplicates(nums_copy)
    assert result == expected
    assert nums_copy[:result] == sorted(set(nums))

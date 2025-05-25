# Difficulty: Easy
# Platform: LeetCode
# LeetCode Problem ID: #26
"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that
each unique element appears only once. The relative order of the elements should be kept the same.
Return the number of unique elements in nums. It must be done with O(1) extra memory.
"""


def remove_duplicates(nums):
    left = 0
    right = left + 1
    while left < len(nums) - 1:
        if nums[left] == nums[right]:
            print("Duplicate values are in position ", left + 1, right + 1)
            nums.remove(nums[left])
        right += 1
        if right == len(nums):
            left += 1
            right = left + 1
    return len(nums)


if __name__ == "__main__":
    input_str = input("Enter the list of elements in array separated by comma")
    input_arr = list(map(int, input_str.split(",")))
    output_len = remove_duplicates(input_arr)
    print(output_len)

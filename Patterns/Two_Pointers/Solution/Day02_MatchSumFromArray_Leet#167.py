# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
# find two numbers such that they add up to a specific target number.
# Return the indices of the two numbers (index1, index2) as an integer
# array [index1, index2] of length 2, where 1 <= index1 < index2 <= numbers.length.
# You must use an algorithm with O(n) time complexity.
def matsum_fromarray(i_nums, t_sum):
    left, right = 0, len(i_nums) - 1
    while left < right:
        calc_sum = i_nums[left] + i_nums[right]
        if calc_sum == t_sum:
            return [left+1, right+1]
        elif calc_sum < t_sum:
            left += 1
        else:
            right -= 1
    return []


if __name__ == "__main__":
    input_str = input("Enter a list of numbers separated by comma")
    input_nums = list(map(int, input_str.split(",")))
    target_sum = input("Enter target sum")
    match_index = matsum_fromarray(list(input_nums),int(target_sum))
    print(match_index)


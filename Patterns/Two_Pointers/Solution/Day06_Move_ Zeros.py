"""
Given an integer array nums, move all 0('s to the end of it
while maintaining the relative order of the non-zero elements.Do this in-place with O(1) extra space.) """


def move_zeros(nums):
    left = 0
    for right in range(0, len(nums)):
        if nums[right] == 0:
            continue
        else:
            nums[left] = nums[right]
            left += 1
        if right == len(nums) - 1:
            nums[left:] = [0] * (len(nums) - left)
    return nums


if __name__ == "__main__":
    input_str = input("Enter the input array elements separated by commas: ")
    input_arr = list(map(int, input_str.split(",")))
    print(move_zeros(input_arr))




"""
Issues in Your Code:
*** Modifying a list while iterating (nums.remove(nums[left])):This shifts the elements
   and corrupts the current indexing of left and right.
   Leads to skipping over elements or IndexError.
*** Extra space (under the hood): remove() internally shifts and reallocates,
    which can be considered as not O(1) in strict interview terms.
*** Returns final length but doesn't maintain valid elements at start of array (nums[:k] might be wrong).
SPACE COMPLEXITY and TIME COMPLEXITY is O(n) for remove function
"""


def remove_duplicates(nums):
    if not nums:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return i + 1


if __name__ == "__main__":
    input_str = input("Enter the list of elements in array separated by comma")
    input_arr = list(map(int, input_str.split(",")))
    output_len = remove_duplicates(input_arr)
    print(output_len, input_arr[0:output_len])

"""
283. Move Zeroes

Given an integer array nums, move all 0's to the end of it
while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

"""


def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """

    i = 0
    last_non_zero_idx = len(nums)    # initialize to be at the end of the list

    while i < last_non_zero_idx:
        if nums[i] == 0:
            nums[i:] = nums[i+1:] + [0]
            last_non_zero_idx -= 1
        else:
            i += 1

    return nums


test_case = [0]
test_case = [0,1,0,3,12]
print(f"Updated list with zeroes at the end = {moveZeroes(test_case)}")

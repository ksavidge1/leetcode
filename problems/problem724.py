"""
724. Find Pivot Index

Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index
is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left.
This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.


Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11

"""

from math import ceil


def pivotIndex(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    # This is somewhat similar to problem 238.
    # We want to make sure we don't re-compute the same additions over and over

    length = len(nums)
    if length == 1:
        return 0    # degenerate case

    sum_l_to_r = 0
    pivot_idx = -1  # initialized

    # we can get all the sums coming from the right, and use these in a separate loop
    rights = [nums[-1]]     # first number has nothing added to it
    for i in range(1, length-1):
        rights.append(nums[-i-1] + rights[i - 1])
    rights_reversed = rights[::-1] + [0]    # add the zero for when we're at the right edge

    for i in range(length):
        sum_r_to_l = rights_reversed[i]
        if sum_l_to_r == sum_r_to_l:
            pivot_idx = i
            break
        sum_l_to_r += nums[i]

    return pivot_idx


test_case = [1,7,3,6,5,6]
test_case = [-1,-1,0,1,1,0]
print(f"Pivot index = {pivotIndex(test_case)}")

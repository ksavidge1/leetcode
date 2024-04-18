"""
643. Maximum Average Subarray I

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
Any answer with a calculation error less than 10^-5 will be accepted.

Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:
Input: nums = [5], k = 1
Output: 5.00000

"""


def findMaxAverage(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: float
    """

    # The sliding window should start with element 0.
    # It should end when the last digit of nums gets included in a subarray

    # Initialize max_avg with the first subarray's average
    curr_sum = sum(nums[:k])
    max_avg = curr_sum / float(k)

    for i in range(1, len(nums) - k + 1):
        # To slide right 1 position, we can drop the first number and add the next
        curr_sum = curr_sum - nums[i - 1] + nums[i + k - 1]
        curr_avg = curr_sum / float(k)

        # Update max_avg if a higher average is found
        if curr_avg > max_avg:
            max_avg = curr_avg

    return max_avg


nums = [1,12,-5,-6,50,3]
k = 4
print(f"Max average of length {k} = {findMaxAverage(nums, k)}")

"""
238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i]
is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.


Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

"""


def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    length = len(nums)

    # This a very readable way to do this while still using O(n) time.
    # It could be more efficient and use less memory

    l_products = [1] * length
    for i in range(1, length):
        l_products[i] = l_products[i - 1] * nums[i - 1]

    r_products = [1] * length
    for i in range(length - 1, 0, -1):
        r_products[i - 1] = r_products[i] * nums[i]

    products = [left * right for left, right in zip(l_products, r_products)]

    return products


list_1 = [2, 3, 4, 5, 6]
print(f"Product Except Self = {productExceptSelf(list_1)}")

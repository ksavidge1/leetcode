"""
2215. Find the Difference of Two Arrays

Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
    - answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
    - answer[1] is a list of all distinct integers in nums2 which are not present in nums1.

Note that the integers in the lists may be returned in any order.

Example 1:
Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]
Explanation:
For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6].

"""


def findDifference(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[List[int]]
    """
    unique_nums1 = list(set(nums1))
    unique_nums2 = list(set(nums2))

    unique_nums1.sort()
    unique_nums2.sort()

    # Initialize
    pos1 = len(unique_nums1) - 1
    pos2 = len(unique_nums2) - 1
    result1 = []
    result2 = []

    while unique_nums1 or unique_nums2:
        num1 = unique_nums1[pos1] if unique_nums1 else float('-inf')
        num2 = unique_nums2[pos2] if unique_nums2 else float('-inf')

        if num1 > num2:
            result1.append(num1)
            unique_nums1.remove(num1)
            pos1 -= 1 if pos1 > 0 else 0
        elif num2 > num1:
            result2.append(num2)
            unique_nums2.remove(num2)
            pos2 -= 1 if pos2 > 0 else 0
        else:
            unique_nums1.remove(num1)
            unique_nums2.remove(num2)
            pos1 -= 1 if pos1 > 0 else 0
            pos2 -= 1 if pos2 > 0 else 0

    return [result1, result2]


nums_1 = [1,2,3]
nums_2 = [4,5,6]
print(f"Unique values in num1 and then in num2 = {findDifference(nums_1, nums_2)}")

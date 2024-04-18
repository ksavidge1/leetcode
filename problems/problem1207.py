"""

1207. Unique number of Occurrences

Given an array of integers arr, return true if the
number of occurrences of each value in the array is unique or false otherwise.


Example 1:
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
"""


def uniqueOccurrences(arr):
    """
    :type arr: List[int]
    :rtype: bool
    """

    # Let's sort up front to simplify things
    arr.sort()

    # Create a dict and store the number of occurrences
    # Initialize using first value. We'll track this as we loop
    prev_num = arr[0]
    nums_and_occurs = {prev_num: 1}

    for num in arr[1:]:
        if num == prev_num:
            nums_and_occurs[num] += 1
        else:
            nums_and_occurs[num] = 1
            prev_num = num

    # Then can check the list of all values versus using a set()
    if len(nums_and_occurs.values()) == len(set(nums_and_occurs.values())):
        return True
    else:
        return False


nums = [1,2]
print(f"Are there a unique number of occurrences for each letter? {uniqueOccurrences(nums)}")

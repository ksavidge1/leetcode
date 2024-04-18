"""
392. Is Subsequence

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string
by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

"""


def isSubsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """

    len_t = len(t)
    pos_t = 0

    for curr_s in s:
        found_s = False

        while pos_t < len_t and not found_s:
            if curr_s == t[pos_t]:
                found_s = True
            pos_t += 1

        if not found_s:
            return False

    return True


s_test = 'axc'
t_test = 'ahbgdc'
print(f"Is '{s_test}' a subsequence of '{t_test}'? "
      f"{isSubsequence(s_test, t_test)}")

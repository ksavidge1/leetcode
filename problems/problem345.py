"""
345. Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:
Input: s = "hello"
Output: "holle"

Example 2:
Input: s = "leetcode"
Output: "leotcede"

"""

vowels = set('aieouAEIOU')


def reverseVowels(s):
    """
    :type s: str
    :rtype: str
    """

    s = list(s)
    l = 0
    r = len(s) - 1
    while l <= r:
        while l <= r and s[l] not in vowels: l += 1
        while l <= r and s[r] not in vowels: r -= 1
        if l > r: break
        s[l], s[r] = s[r], s[l]
        l, r = l + 1, r - 1
    return ''.join(s)


str_1 = 'tEmpoRaL'
print(f"String with vowels reversed = {reverseVowels(str_1)}")

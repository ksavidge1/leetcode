"""
1071. Greatest Common Divisor of Strings

For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t
(i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2

Example 1:
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:
Input: str1 = "LEET", str2 = "CODE"
Output: ""

"""


def gcd_of_strings(str1, str2):
    """
    :type str1: str
    :type str2: str
    :rtype: str
    """

    # Find divisible for one string at a time (may only be the full string)
    str1_divisors = compute_divisors_one_str(str1)
    str2_divisors = compute_divisors_one_str(str2)

    longest_match = ""  # initialize as having no matches
    # Arbitrary whether we go through divisors in str1 or str2 in the loop
    for divisor in str1_divisors:
        if divisor in str2_divisors:
            longest_match = divisor

    return longest_match


def compute_divisors_one_str(input_str):
    """
    :type input_str: str
    :rtype: list
    """
    length = len(input_str)

    divisors = []  # initialize
    for n in range(1, length + 1):
        if length % n == 0:    # break the string down only when divisible
            num_repeats = int(length / n)
            piece = input_str[:n]
            if piece * num_repeats == input_str:
                divisors.append(piece)

    return divisors


str_1 = "ABCABCABC"
str_2 = "ABCABC"
print(f"longest matching divisor = {gcd_of_strings(str_1, str_2)}")

"""
You are given two strings word1 and word2.

Merge the strings by adding letters in alternating order, starting with word1.

If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

"""


def merge_alternately(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: str
    """
    output_word = ""    # we'll build this as we go

    len_word1 = len(word1)
    len_word2 = len(word2)
    max_len = max(len_word1, len_word2)

    for i in range(max_len):
        if i < len_word1:
            output_word += word1[i]

        if i < len_word2:
            output_word += word2[i]

    return output_word


print(merge_alternately("test", "testnew"))

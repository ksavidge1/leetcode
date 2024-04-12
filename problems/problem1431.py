"""
Kids with the Greatest Number of Candies

There are n kids with candies.

You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has,
and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies,
they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.

"""


def kids_with_candies(candies, extraCandies):
    """
    :type candies: List[int]
    :type extraCandies: int
    :rtype: List[bool]
    """

    result = []
    max_candies = max(candies)

    # Find the result of whether adding extra_candies to each kid will get them more than the current max
    for kid_candies in candies:
        new_candies = kid_candies + extraCandies
        result.append(new_candies >= max_candies)

    return result


kids_with_candies([5, 3, 5, 1], 3)


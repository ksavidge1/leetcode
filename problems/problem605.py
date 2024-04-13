"""
You have a long flowerbed in which some of the plots are planted, and some are not.

However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty,
and an integer n, return true if n new flowers can be planted in the flowerbed
without violating the no-adjacent-flowers rule and false otherwise.

"""


def canPlaceFlowers(flowerbed, n):
    """
    :type flowerbed: List[int]
    :type n: int
    :rtype: bool
    """
    # Iterate through the flower bed and count how many gaps are available
    # It's helpful to update flowerbed throughout, putting in the newly placed flowers
    num_gaps = 0    # incremented once a gap is found
    pos = 0
    prev = 0    # helpful as we iterate so we don't have to look backwards
    flowerbed_ext = flowerbed + [0]  # can treat the position 1 after last as "0"

    while pos < (len(flowerbed)):
        if flowerbed[pos] == 1:    # can't place a flower next to this one
            prev = 1
        else:                      # not currently in a place with a flower
            if prev == 0 and flowerbed_ext[pos+1] == 0:
                num_gaps += 1
                prev = 1
            elif prev == 1:
                prev = 0    # can't place a flower after the previous one, but can set prev = 0 for next iteration

        pos += 1

    return num_gaps >= n


flowerbed = [1,0,0,0,1,0,0]
new_flowers = 2
print(f'# of available gaps >= {new_flowers}? {canPlaceFlowers(flowerbed, new_flowers)}')



"""
735. Asteroid Collision

We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size,
and the sign represents its direction (positive meaning right, negative meaning left).
Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions.
If two asteroids meet, the smaller one will explode.
If both are the same size, both will explode.
Two asteroids moving in the same direction will never meet.

Example 1:
Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

"""


def asteroidCollision(asteroids):
    """
    :type asteroids: List[int]
    :rtype: List[int]
    """

    i = 0

    while i < len(asteroids) - 1:
        if asteroids[i] < 0:
            # Can't be a collision because it's moving left
            i += 1
        elif (asteroids[i] == abs(asteroids[i + 1])) and (asteroids[i + 1] < 0):
            # Moving toward each other and same size
            asteroids.pop(i), asteroids.pop(i)
            if i != 0:
                i -= 1
        elif asteroids[i + 1] < 0:
            # Moving toward each but not same size
            if asteroids[i] > abs(asteroids[i + 1]):
                asteroids.pop(i+1)
            else:
                asteroids.pop(i)
                if i != 0:
                    i -= 1
        else:
            # Both moving right, so no collision
            i += 1

    return asteroids


asteroids_test = [1,1,-1,-2]
print(f"Remaining asteroids: {asteroidCollision(asteroids_test)}")


"""
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.



Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
"""


def asterooid_collision(asteroids):
    stack = []
    for i in asteroids:
        while stack and i < 0 < stack[-1]:
            if abs(i) > stack[-1]:
                stack.pop()
                continue
            elif abs(i) == stack[-1]:
                stack.pop()
            break
        else:
            stack.append(i)
    return stack


print(asterooid_collision([5,10,-5]))
print(asterooid_collision([-8, 2,-8,-8]))
print(asterooid_collision([10,2,-5]))
print(asterooid_collision([-2,-2,1,-2]))
from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        collisions = []
        for asteroid in asteroids:
            while collisions and asteroid < 0 < collisions[-1]:
                if collisions[-1] < -asteroid:
                    collisions.pop()
                    continue
                elif collisions[-1] == -asteroid:
                    collisions.pop()
                break
            else:
                collisions.append(asteroid)
        return collisions
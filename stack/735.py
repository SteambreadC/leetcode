from typing import Optional, List
from collections import deque


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        i = 0
        new = []
        while i < len(asteroids):
            if not new or new[-1] < 0 or asteroids[i] > 0:
                new.append(asteroids[i])
                i += 1
            else:
                asterN = asteroids[i]
                asterP = new[-1]
                while new and new[-1] >0 > asterN:
                    if new[-1] < -asterN:
                        new.pop()
                        continue
                    elif new[-1] == -asterN:
                        asterP = new.pop(-1)
                    i += 1
                    break
        return new

    def asteroidCollision_oldVersion(self, asteroids: List[int]) -> List[int]:
        i = 0
        new = []
        while i < len(asteroids):
            if not new or new[-1] < 0 or asteroids[i] > 0:
                new.append(asteroids[i])
                i += 1
            else:
                asterN = abs(asteroids[i])
                asterP = new.pop(-1)
                while new and asterN > asterP > 0:
                    asterP = new.pop(-1)
                if asterP != asterN:
                    if asterN > asterP > 0:
                        new.append(-asterN)
                    else:
                        new.append(asterP)
                        if asterP < 0:
                            new.append(-asterN)
                i += 1
        return new


if __name__ == '__main__':
    sol = Solution()
    res = sol.asteroidCollision_oldVersion([-5,-6, 1, -2, -2, -2])
    print(res)

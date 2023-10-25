from typing import Optional, List
from collections import deque


def getChannelRating(views: List[int]) -> int:
    mod = pow(10, 9) + 7
    rating = 0
    k, l = len(views)
    for k in range(l-1, 2):
        for i in range(0, l-k):
            sub = views[i:i+k-1]
            v1 = sub[0]^sub[-1]
            for j in range()




    return rating


if __name__ == '__main__':
    res = getChannelRating([])
    print(res)

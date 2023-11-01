from typing import Optional, List
from collections import deque

def findMinEqual(blocksA:List[int], blocksB:List[int]):
    sumA, sumB = sum(blocksA), sum(blocksB)
    zerosA, zerosB = blocksA.count(0), blocksB.count(0)
    sumA += zerosA
    sumB += zerosB
    return max(sumB, sumA)


if __name__ == '__main__':
    res = findMinEqual([1,0,2], [1,3,0,0])
    print(res)

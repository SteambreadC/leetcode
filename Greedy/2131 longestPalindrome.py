import collections
from typing import List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        # Time complexity is O(n^2), which is too large for this problem.
        revCount = 0
        palinCount = 0
        i = 0
        while i < len(words):
            reverse = words[i][::-1]
            for j in range(i + 1, len(words)):
                if words[j] == reverse:
                    revCount += 1
                    del words[j]
                    del words[i]
                    i -= 1
                    break
            i += 1
        for j in range(len(words)):
            if words[j][::-1] == words[j]:
                palinCount = 1
        return revCount * 4 + 2 * palinCount

    def longestPalindrome_hash(self, words: List[str]) -> int:
        # We use a hash table to reduce time complexity.
        # Use this to learn about dictionary and counter.
        counter = collections.Counter(words)
        pairCount = 0
        singleCount = 0
        for word, count in counter.items():
            if word == word[::-1]:
                if singleCount == 0 and count % 2 == 1:
                    singleCount = 1
                pairCount += int(count/2)
            else:
                reverse = word[::-1]
                if reverse in counter:
                    revCount = counter[reverse]
                    pairCount += min(count, revCount)
                    counter[word] = 0
                    counter[reverse] = 0
        return pairCount * 4 + singleCount * 2


if __name__ == '__main__':
    sol = Solution()
    res = sol.longestPalindrome_hash(["ab","ty","yt","lc","cl","ab"])
    print(res)

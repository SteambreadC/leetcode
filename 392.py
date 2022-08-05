class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptr=0
        ext=False

        for i in range(len(s)):
            for j in range(ptr, len(t)):
                if s[i] == t[j]:
                    ptr = j+1
                    ext=True
                    break
            if ext==False: return False
            else: ext=False

        return True

if __name__ == '__main__':
    sol = Solution()
    print(sol.isSubsequence("abc","ahdgdc"))

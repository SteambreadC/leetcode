class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        asc = [0] * 128
        iso = [0] * len(s)
        iso2 = [0] * len(t)
        num = 0

        for i in range(len(s)):
            if asc[ord(s[i])-97] == 0:
                num += 1
                asc[ord(s[i]) - 97] = num
            iso[i] = asc[ord(s[i])-97]
        print(iso)
        num = 0
        asc = [0] * 128
        for i in range(len(t)):
            if asc[ord(t[i])-97] == 0:
                num += 1
                asc[ord(t[i]) - 97] = num
            iso2[i] = asc[ord(t[i])-97]
        print(iso2)
        return iso == iso2

if __name__ == '__main__':
    sol = Solution()
    print(sol.isIsomorphic("erfew", "bbbbb"))

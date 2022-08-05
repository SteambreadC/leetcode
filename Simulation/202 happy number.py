class Solution:
    def isHappy(self, n: int) -> bool:
        num = n
        processList = list()
        while num != 1:
            if num in processList:
                return False
            else:
                processList.append(num)
                intToStr = str(num)
                num = 0
                for i in range(len(intToStr)):
                    num += int(intToStr[i]) ** 2

        return True

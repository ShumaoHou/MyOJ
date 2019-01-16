class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        sumStr = str(int(a) + int(b))
        sumList = [int(sumStr[i]) for i in range(len(sumStr))]
        for i in range(0, len(sumList) - 1):
            k = len(sumList) - i - 1
            if sumList[k] >= 2:
                sumList[k] -= 2
                sumList[k - 1] += 1
        if sumList[0] >= 2:
            sumList[0] -= 2
            sumList.insert(0, 1)
        res = ""
        for i in range(len(sumList)):
            res += str(sumList[i])
        return res
if __name__ == '__main__':
    a = input()
    b = input()
    print(Solution().addBinary(a, b))
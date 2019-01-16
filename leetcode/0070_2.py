'''
爬楼梯
斐波那契数列
'''
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        s1 = 1
        s2 = 2
        for i in range(3, n + 1):
            s = s1 + s2
            s1 = s2
            s2 = s
        return s
if __name__ == '__main__':
    n = int(input())
    print(Solution().climbStairs(n))
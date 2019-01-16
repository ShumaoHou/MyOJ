'''
爬楼梯
记忆化搜索
'''
memo = []
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        global memo
        memo = [-1] * (n + 1)
        return self.getClimb(n)

    def getClimb(self, n):
        global memo
        if n == 1:
            return 1
        elif n == 2:
            return 2
        if memo[n] == -1:
            memo[n] = self.getClimb(n - 1) + self.getClimb(n - 2)
        return memo[n]
if __name__ == '__main__':
    n = int(input())
    print(Solution().climbStairs(n))
'''
爬楼梯
递归算法
'''
from functools import lru_cache
class Solution:
    @lru_cache(10 ** 8)
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
if __name__ == '__main__':
    n = int(input())
    print(Solution().climbStairs(n))
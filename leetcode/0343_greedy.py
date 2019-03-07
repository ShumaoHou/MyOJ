"""
给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。
示例 1:
输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。
示例 2:
输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
说明: 你可以假设 n 不小于 2 且不大于 58。
"""


class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 贪婪算法
        if n <2 :
            return 0
        elif n == 2:
            return 1
        elif n == 3:
            return 2
        timesOf3 = n // 3
        # 如果最后剩下1，则加个3变成4，4>1*3
        if n - timesOf3 * 3 == 1:
            timesOf3 -= 1
        timesOf2 = (n - timesOf3*3) // 2
        return pow(3, timesOf3) * pow(2, timesOf2)

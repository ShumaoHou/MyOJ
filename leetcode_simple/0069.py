class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x
        r = x
        while r * r > x:
            r = (r + x / r) // 2
        return int(r)
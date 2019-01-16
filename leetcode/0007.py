'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
示例 1:
输入: 123
输出: 321
 示例 2:
输入: -123
输出: -321
示例 3:
输入: 120
输出: 21
注意:
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^(31 − 1)]。请根据这个假设，如果反转后整数溢出那么就返回 0。
'''
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_neg = False
        if x < 0:
            s = str(-x)
            is_neg = True
        else:
            s = str(x)
        l = list(s)
        l.reverse()
        if l[0] == "0" and len(l) > 1:
            l = l[1:]
        s = "".join(l)
        num = int(s)
        if is_neg:
            num = - num
        if num > pow(2, 31) - 1 or num < - pow(2, 31):
            num = 0
        return num

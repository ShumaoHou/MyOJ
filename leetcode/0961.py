"""
在大小为 2N 的数组 A 中有 N+1 个不同的元素，其中有一个元素重复了 N 次。
返回重复了 N 次的那个元素。
示例 1：
输入：[1,2,3,3]
输出：3
示例 2：
输入：[2,1,2,5,3,2]
输出：2
示例 3：
输入：[5,1,5,2,5,3,5,4]
输出：5
提示：
4 <= A.length <= 10000
0 <= A[i] < 10000
A.length 为偶数
"""


class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        """
        分析题目可知，总共有2N个元素，N+1个不同元素，1个重复N次元素，
        那么剩下的N个元素就是唯一不重复的。只需要找出出现两次的元素即可。
        """
        B = []
        res = -1
        for i in A:
            if i in B:
                res = i
                break
            else:
                B.append(i)
        return res

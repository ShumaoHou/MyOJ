"""
给定一个非负整数数组 A，返回一个由 A 的所有偶数元素组成的数组，后面跟 A 的所有奇数元素。
你可以返回满足此条件的任何数组作为答案。
示例：
输入：[3,1,2,4]
输出：[2,4,3,1]
输出 [4,2,3,1]，[2,4,1,3] 和 [4,2,1,3] 也会被接受。
提示：
1 <= A.length <= 5000
0 <= A[i] <= 5000

3 1 2 4

"""


class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        # B = []
        # C = []
        # for i in A:
        #     if i % 2 == 0:
        #         B.append(i)
        #     else:
        #         C.append(i)
        # # B.extend(C)
        # return B + C

        i = 0
        for j in range(len(A)):
            # 将偶数和开始位置交换
            if A[j] % 2 == 0:
                A[i], A[j] = A[j], A[i]
                i += 1
        return A


if __name__ == '__main__':
    a = list(map(int, input().split()))
    print(Solution().sortArrayByParity(a))
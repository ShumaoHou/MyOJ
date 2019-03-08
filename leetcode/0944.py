"""
给定由 N 个小写字母字符串组成的数组 A，其中每个字符串长度相等。
选取一个删除索引序列，对于 A 中的每个字符串，删除对应每个索引处的字符。 所余下的字符串行从上往下读形成列。
比如，有 A = ["abcdef", "uvwxyz"]，删除索引序列 {0, 2, 3}，删除后 A 为["bef", "vyz"]， A 的列分别为["b","v"], ["e","y"], ["f","z"]。
（形式上，第 n 列为 [A[0][n], A[1][n], ..., A[A.length-1][n]]）。
假设，我们选择了一组删除索引 D，那么在执行删除操作之后，A 中所剩余的每一列都必须是 非降序 排列的，然后请你返回 D.length 的最小可能值。
示例 1：
输入：["cba", "daf", "ghi"]
输出：1
解释：
当选择 D = {1}，删除后 A 的列为：["c","d","g"] 和 ["a","f","i"]，均为非降序排列。
若选择 D = {}，那么 A 的列 ["b","a","h"] 就不是非降序排列了。
示例 2：
输入：["a", "b"]
输出：0
解释：D = {}
示例 3：
输入：["zyx", "wvu", "tsr"]
输出：3
解释：D = {0, 1, 2}
提示：
1 <= A.length <= 100
1 <= A[i].length <= 1000
"""
"""
其实是计算有多少个非降序列：
输入：["zyxa", "wvub", "tsrc"] 可以转换成
z y x a
w v u b
t s r c
这样的矩阵，然后看它每一列是否从上到下为降序，
例如 0、1、2列为非降序，3列为降序
是降序则记录它的列序号，并删掉。
输出有几个这样的降序列。
"""


class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
        如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
        """
        result = 0
        for col in zip(*A):
            # print(col)
            if sorted(col) != list(col):
                result += 1
        return result


if __name__ == '__main__':
    A= ["abcdzf", "uvwxyz"]
    print(Solution().minDeletionSize(A))

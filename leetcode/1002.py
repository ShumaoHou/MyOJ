"""
给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。
例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。
你可以按任意顺序返回答案。
示例 1：
输入：["bella","label","roller"]
输出：["e","l","l"]
示例 2：
输入：["cool","lock","cook"]
输出：["c","o"]
提示：
1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] 是小写字母

bella label roller
cool lock cook
"""


class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        res = []
        for i in A[0]:  # 常用字符一定包含在第一个字符串中
            isRes = True  # 是否i为常用字符
            for j in range(1, len(A)):
                if i not in A[j]:
                    isRes = False
                    break
            # 如果是常用字符，则每个字符串都删掉一个常用字符
            if isRes:
                res.append(i)
                for j in range(1, len(A)):
                    index = A[j].find(i)
                    A[j] = A[j][:index] + A[j][index + 1:]
        return res


if __name__ == '__main__':
    a = list(map(str, input().split()))
    print(Solution().commonChars(a))
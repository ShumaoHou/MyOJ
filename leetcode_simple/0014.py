'''
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
示例 1:
输入: ["flower","flow","flight"]
输出: "fl"
示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:
所有输入只包含小写字母 a-z 。
'''
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        comStr = ""
        if len(strs) == 0:
            return comStr
        firstStr = strs[0]
        for i in range(len(firstStr)):
            ch = firstStr[i: i + 1]
            for j in range(len(strs)):
                nowStr = strs[j]
                if len(nowStr) < i:
                    return comStr
                if nowStr[i : i + 1] != ch:
                    return comStr
            comStr += ch
        return comStr



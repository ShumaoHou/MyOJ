class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        if len(haystack) < len(needle):
            return -1
        k = 0
        for i in range(len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    k = 0
                    break
                k += 1
                if k == len(needle):
                    return i
        return -1
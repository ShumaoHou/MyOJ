class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s.strip()) == 0:
            return 0
        list = s.strip().split(' ')
        return len(list[-1])

if __name__ == '__main__':
    s = input()
    print(Solution().lengthOfLastWord(s))
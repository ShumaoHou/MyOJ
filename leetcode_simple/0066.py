class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits == [0]:
            return [1]
        digits[-1] += 1
        for i in reversed(range(1, len(digits))):
            if digits[i] == 10:
                digits[i - 1] += 1
                digits[i] = 0
        if digits[0] == 10:
            digits[0] = 0
            digits.insert(0, 1)
        return digits
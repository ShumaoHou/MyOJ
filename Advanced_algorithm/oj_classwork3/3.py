'''
最长字符串，以ASCII码的非递减顺序和算术级数
https://www.geeksforgeeks.org/longest-string-in-non-decreasing-order-of-ascii-code-and-in-arithmetic-progression/
描述
Archana is very fond f strings. She likes to solve many questions related to strings.
She comes across a problem which she is unable to solve. Help her to solve.
The problem is as follows:-Given is a string of length L.
Her task is to find the longest string from the given string with characters arranged in descending order of their ASCII code and in arithmetic progression.
She wants the common difference should be as low as possible(at least 1) and the characters of the string to be of higher ASCII value.
输入
The first line of input contains an integer T denoting the number of test cases. Each test contains a string s of lengthL.
1<= T <= 100
3<= L <=1000
A<=s[i]<=Z
The string contains minimum three different characters.
输出
For each test case print the longest string.
Case 1:Two strings of maximum length are possible- “CBA” and “RPQ”.
But he wants the string to be of higher ASCII value therefore, the output is “RPQ”.Case 2:The String of maximum length is “JGDA”.
输入样例
2
ABCPQR
ADGJPRT
输出样例
RQP
JGDA
'''


def findLongestString(A):
    maxLen = 0
    bestStartChar = 0
    minCommonDifference = 3000
    mp = dict()
    for i in range(len(A)):
        mp[A[i]] = True
    for start in range(ord('Z'), ord('A') - 1, -1):
        if chr(start) in mp.keys():
            for diff in range(1,13):
                currLen = 1
                ch = start - diff
                while(ch >= ord('A')):
                    if chr(ch) in mp.keys():
                        currLen += 1
                    else:
                        break
                    ch -= diff
                if currLen > maxLen or (currLen == maxLen and diff < minCommonDifference):
                    minCommonDifference = diff
                    maxLen = currLen
                    bestStartChar = start
    longestString = ""
    i = bestStartChar
    while(i >= (bestStartChar - (maxLen - 1) * minCommonDifference)):
        longestString += chr(i)
        i -= minCommonDifference
    return longestString

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        A = str(input())
        print(findLongestString(A))

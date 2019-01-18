'''
字符串首尾相连组成圈
描述
Given an array of strings A[ ], determine if the strings can be chained together to form a circle.
A string X can be chained together with another string Y if the last character of X is same as first character of Y.
If every string of the array can be chained, it will form a circle.For eg for the array
arr[] = {"for", "geek", "rig", "kaf"} the answer will be Yes as the given strings can be chained as "for", "rig", "geek" and "kaf"
输入
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow.
The first line of each test case contains a positive integer N, denoting the size of the array.
The second line of each test case contains a N space seprated strings, denoting the elements of the array A[ ].
1 <= T <= 100
0 < N <= 30
0 < A[i] <= 10
输出
If chain can be formed, then print 1, else print 0.
输入样例
2
3
abc bcd cdf
4
ab bc cd da
输出样例
0
1
'''
def isCircle(A):
    # 只有一个字符串
    if len(A) == 1:
        strA = A[0]
        if strA[0:1] == strA[-1]:
            return 1
        else:
            return 0
    start = A[0]
    count = 0
    now = A[0]
    A.remove(now)
    while len(A) != 0:
        # print(A)
        hasC = False
        # 遍历查找匹配字符串
        for strB in A:
            # 当前字符串结尾等于遍历中的字符串开头
            if now[-1] == strB[0:1]:
                # print(strB)
                if len(A) == 1:
                    if strB[-1] != start[0:1]:
                        return 0
                now = strB
                A.remove(strB)
                count += 1
                hasC = True
                break
        if not hasC :
            return 0
    return 1

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        N = int(input())
        A = list(map(str, input().split()))
        print(isCircle(A))
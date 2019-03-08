"""
帮帮Mike
描述
Mike is a lawyer with the gift of photographic memory.
 He is so good with it that he can tell you all the numbers on a sheet of paper by having a look at it without any mistake.
 Mike is also brilliant with subsets so he thought of giving a challenge based on his skill and knowledge to Rachael.
 Mike knows how many subset are possible in an array of N integers.
 The subsets may or may not have the different sum.
 The challenge is to find the maximum sum produced by any subset under the condition:
The elements present in the subset should not have any digit in common.
Note: Subset {12, 36, 45} does not have any digit in common and Subset {12, 22, 35 } have digits in common.
Rachael find it difficult to win the challenge and is asking your help. Can you help her out in winning this challenge?
输入
First Line of the input consist of an integer T denoting the number of test cases.
Then T test cases follow. Each test case consist of a numbe N denoting the length of the array.
Second line of each test case consist of N space separated integers denoting the array elements.
Constraints:
1 <= T <= 100
1 <= N <= 100
1 <= array elements <= 100000
输出
Corresponding to each test case, print output in the new line.
输入样例 1
1
3
12 22 35
输出样例 1
57
"""


def cor_bin(n):
    ans = 0
    for c in str(n):
        ans |= 1 << ord(c) - ord('0')
    return ans


def solve(A, dp, n, flags):
    if n < 0: return 0
    if dp[n][flags]: return dp[n][flags]
    dp[n][flags] = solve(A, dp, n - 1, flags)
    a = cor_bin(A[n])
    if flags ^ a == flags - a:
        dp[n][flags] = max(dp[n][flags], A[n] + solve(A, dp, n - 1, flags ^ a))
    return dp[n][flags]


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        S = input()
        S = S.split()
        A = [int(item) for item in S]
        dp = [[None] * 2 ** 10 for _ in range(n)]
        print(solve(A, dp, n - 1, 2 ** 10 - 1))

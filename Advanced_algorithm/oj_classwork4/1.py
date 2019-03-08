"""
帮帮Stish
描述
Satish wants to prepare for tommorow's exam .
He knows the distribution of marks for the subject along with time to learn the concepts.
You are given remaining time for the exam along with marks for each topic and passing marks for the subject.
Find the max marks Satish can attain by studing max no of topic in max no hours not excedding (p) .
输入
The first line of input contains the number of testcases t.
The first line of each testcase contains the no of topics(n) ,
time remaining for exam(h) in hour and passing marks(p).
Each 'n' lines contain u(time to learn topic) and v(weightage of topic in exam) .
输出
For each test case print "YES" along with time taken or "NO".
Constraints:
1<=t<=100
1<=n<=300
1<=h<=150
1<=p<=35
1<=u,v<=25
输入样例 1
1
5 40 21
12 10
16 10
20 10
24 10
8 3
输出样例 1
YES 36
"""
# 背包问题
if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        n, h, P = map(int, input().split())
        time = []
        weights = []
        for N in range(n):
            u, v = map(int, input().split())
            time.append(u)
            weights.append(v)
        # 前i个课程，当前剩余时间j，的分数
        dp = [[0 for j in range(h + 1)] for i in range(n + 1)]
        p = [[0 for j in range(h + 1)] for i in range(n + 1)]
        for i in range(0, n + 1):
            for j in range(0, h + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif j < time[i - 1]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    a = dp[i - 1][j - time[i - 1]] + weights[i - 1]
                    b = dp[i - 1][j]
                    dp[i][j] = max(b, a)
        a = n
        b = h
        timeTaken = 0
        while a != 0:
            if dp[a][b] != dp[a - 1][b]:
                timeTaken += time[a - 1]
                a -= 1
                b -= time[a]
            else:
                a -= 1
        res = ""
        if dp[n][h] >= P:
            res = "YES " + str(timeTaken)
        else:
            res = "NO"
        print(res)

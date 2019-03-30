"""
路上的球
描述
There are two parallel roads, each containing N and M buckets, respectively.
Each bucket may contain some balls.
The buckets on both roads are kept in such a way
that they are sorted according to the number of balls in them.
Geek starts from the end of the road which has the bucket with a lower number of balls
(i.e. if buckets are sorted in increasing order, then geek will start from the left side of the road).
The geek can change the road only at the point of intersection
(which means, buckets with the same number of balls on two roads).
Now you need to help Geek to collect the maximum number of balls.
输入
The first line of input contains T denoting the number of test cases.
The first line of each test case contains two integers N and M,
denoting the number of buckets on road1 and road2 respectively.
2nd line of each test case contains N integers, number of balls in buckets on the first road.
3rd line of each test case contains M integers, number of balls in buckets on the second road.
Constraints:1<= T <= 1000，1<= N <= 10^3，1<= M <=10^3，0<= A[i],B[i]<=10^6
输出
For each test case output a single line containing the maximum possible balls that Geek can collect.
输入样例 1
1
5 5
1 4 5 6 8
2 3 4 6 9
输出样例 1
29
Explanation:

The path with maximum sum is (2,3,4)[5,6](9).
Integers in [] are the buckets of first road and in () are the buckets of second road.
 So, max balls geek can collect is 29.
"""


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        n_balls = list(map(int, input().split()))
        m_balls = list(map(int, input().split()))
        # 找出the point of intersection
        com = []
        i, j = 0, 0
        while i < n and j < m:
            if n_balls[i] < m_balls[j]:
                i += 1
            elif n_balls[i] > m_balls[j]:
                j += 1
            else:
                com.append(n_balls[i])
                i += 1
                j += 1

        i, j, s = 0, 0, 0
        for x in com:
            # 计算交叉点之间的最大值
            a, b = 0, 0
            while i < n:
                a += n_balls[i]
                i += 1
                if i == n or x < n_balls[i]:
                    break
            while j < m:
                b += m_balls[j]
                j += 1
                if j == m or x < m_balls[j]:
                    break
            s += max(a, b)
        # 最后一个交叉点之后的值
        a = sum(n_balls[i:])
        b = sum(m_balls[j:])
        s += max(a, b)
        print(s)

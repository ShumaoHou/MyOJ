"""
时间分隔
描述
Given arrival and departure times of all trains that reach a railway station.
Your task is to find the minimum number of platforms required for the railway station so that no train waits.
Note: Consider that all the trains arrive on the same day and leave on the same day.
 Also, arrival and departure times must not be same for a train.
输入
The first line of input contains T, the number of test cases.
For each test case, first line will contain an integer N,
the number of trains. Next two lines will consist of N space separated time intervals denoting arrival and departure times respectively.
Note: Time intervals are in the 24-hourformat(hhmm),
preceding zeros are insignificant. 200 means 2:00.
Consider the example for better understanding of input.
Constraints:1 <= T <= 100，1 <= N <= 1000，1 <= A[i] < D[i] <= 2359
输出
For each test case, print the minimum number of platforms required for the trains to arrive and depart safely.
输入样例 1
1
6
900  940 950  1100 1500 1800
910 1200 1120 1130 1900 2000
输出样例 1
3
"""


def find_min(a, d, n):
    a.sort()
    d.sort()
    # 平台至少一个
    plat = 1
    res = 1
    # 到达时间指标
    i = 1
    # 离开时间指标
    j = 0
    while i < n and j < n:
        # 到达和离开时间有重合
        if a[i] < d[j]:
            plat += 1
            i += 1
            res = max(res, plat)
        else:
            plat -= 1
            j += 1
    return res


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a_times = list(map(int, input().split()))
        d_times = list(map(int, input().split()))
        print(find_min(a_times, d_times, n))

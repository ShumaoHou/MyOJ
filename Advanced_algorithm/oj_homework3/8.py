"""
拓扑排序解的个数
给定有向无环图中所有边，计算图的拓扑排序解的个数。
输入第一行为用例个数，后面每一行表示一个图中的所有边，边的起点和终点用空格隔开，边之间使用逗号隔开。
输出拓扑排序解的个数。
输入样例
1
a c,b c,c d,d e,d f,e g,f g
输出样例
4
"""


def inputPre():
    global name, pre, m, n
    for i in range(m):
        v = 0
        u = 0
        while u < n:
            if p[i][0] == name[u]:
                break
            else:
                u += 1
        if u == n:
            name.append(p[i][0])
            n += 1
        while v < n:
            if p[i][1] == name[v]:
                break
            else:
                v += 1
        if v == n:
            name.append(p[i][1])
            n += 1
        pre[v] |= (1 << u)


def solve():
    global dp, n
    dp[0] = 1
    for s in range(1 << n):
        if dp[s] != 0:
            for i in range(n):
                if ((s & pre[i]) == pre[i]) and not (s & (1 << i)):
                    dp[s | (1 << i)] += dp[s]
    print(dp[(1 << n) - 1])


if __name__ == '__main__':
    N = int(input())
    for k in range(N):
        pairs = list(map(str, input().split(",")))  # 起点终点对集合
        m = len(pairs)
        n = 0
        p = []  # 存储起点终点对
        for i in range(m):
            pair = pairs[i].split()
            p.append(pair)
        name = []
        size = 13
        pre = [0 for i in range(size)]
        dp = [0 for i in range(1 << size)]
        inputPre()
        solve()

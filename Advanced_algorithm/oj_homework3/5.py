"""
深度优先遍历
按照给定的起始顶点深度优先遍历给定的无向图，尝试所有可能的遍历方式，打印遍历过程中出现的最大深度。
输入: 第一行是用例个数，后面每个用例使用多行表示，
用例的第一行是图中节点的个数n和起始点，用空格隔开，
后面n+1行为图的邻接矩阵，其中第一行为节点名称。值之间使用空格隔开。
输出: 深度优先遍历中遇到的最大深度。
输入样例
1
4 a
a b c d
a 0 1 1 0
b 1 0 1 0
c 1 1 0 1
d 0 0 1 0
输出样例
4
"""
"""
1
4 c
a b c d
a 0 1 1 0
b 1 0 1 0
c 1 1 0 1
d 0 0 1 0
p:
  a b c d
a 0 1 1 0
b 1 0 1 0
c 1 1 0 1
d 0 0 1 0
"""


def DFS(s, d):
    global max
    visited[s] = 1  # 起始节点标记访问
    d += 1
    if d > max:
        max = d
    for j in range(n):
        if p[s][j] == "1" and visited[j] == 0:
            DFS(j, d)
            visited[j] = 0  # 寻找所有路径的关键一步


if __name__ == '__main__':
    N = int(input())
    for k in range(N):
        n, start = map(str, input().split())
        n = int(n)
        names = list(map(str, input().split()))  # 节点名称数组，0..n-1
        p = []  # 邻接矩阵，0..n-1，0..n-1
        pDict = dict()  # 节点名称字典，0..n-1 ，名称-行数
        for i in range(n):
            row = list(map(str, input().split()))
            pDict[row[0]] = i
            p.append(row[1:])
        visited = [0 for i in range(n)]  # 初始化访问数组
        max = 0
        path = []  # 路径
        DFS(pDict[start], 0)
        print(max)

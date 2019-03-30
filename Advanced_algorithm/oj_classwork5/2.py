"""
格子里的整数
描述
Given a square grid of size n, each cell of which contains integer cost
which represents a cost to traverse through that cell,
we need to find a path from top left cell to bottom right cell by which total cost incurred is minimum.
Note : It is assumed that negative cost cycles do not exist in input matrix.
输入
The first line of input will contain number of test cases T.
Then T test cases follow . Each test case contains 2 lines.
The first line of each test case contains an integer n denoting the size of the grid.
Next line of each test contains a single line containing N*N space separated integers depecting cost of respective cell from (0,0) to (n,n).
Constraints:1<=T<=50，1<= n<= 50
输出
For each test case output a single integer depecting the minimum cost to reach the destination.
输入样例 1
2
5
31 100 65 12 18 10 13 47 157 6 100 113 174 11 33 88 124 41 20 140 99 32 111 41 20
2
42 93 7 14
输出样例 1
327
63
"""

x = [-1, 0, 1, 0]
y = [0, -1, 0, 1]
cases = int(input())
for t in range(cases):
    n = int(input())
    graph = list(map(int, input().split()))
    graph = [[graph[n * i + j] for i in range(n)] for j in range(n)]
    dist = [[float("Inf")] * n for i in range(n)]
    dist[0][0] = graph[0][0]
    nodeset = set(())
    nodeset.add((graph[0][0], 0, 0))


    def isValid(i, j):
        return 0 <= i < n and 0 <= j < n


    while nodeset:
        minnode = min(nodeset)
        d, i, j = minnode
        nodeset.remove(minnode)
        for k in range(4):
            X, Y = i + x[k], j + y[k]
            if isValid(X, Y):
                if dist[X][Y] > dist[i][j] + graph[X][Y]:
                    #                     if dist[X][Y]!=float("Inf"):
                    #                         nodeset.remove((dist[X][Y],X,Y))
                    dist[X][Y] = dist[i][j] + graph[X][Y]
                    nodeset.add((dist[X][Y], X, Y))
    print(dist[n - 1][n - 1])

'''
广度优先遍历图
按照给定的起始顶点广度优先遍历图，每一次通过字母顺序选择顶点查找下一层邻接点，打印遍历顺序。
输入第一行为测试用例个数，后面每一个用例用多行表示，用例第一行是节点个数n和开始顶点，
用空格隔开，后面n+1行为图的邻接矩阵，其中第一行为节点名称。值之间使用空格隔开。
输出遍历顺序，用空格隔开
输入样例
1
4 a
a b c d
a 0 1 1 0
b 1 0 1 0
c 1 1 0 1
d 0 0 1 0
输出样例
a b c d
'''
'''
p:
  a b c d
a 0 1 1 0
b 1 0 1 0
c 1 1 0 1
d 0 0 1 0
'''
def BFS(s, n):
    visited = [0 for i in range(n)] # 初始化访问数组
    visited[s] = 1 # 起始节点标记访问
    Q = []
    front = rear = -1
    rear += 1
    Q.append(s) # 起始节点入队列
    res = names[s] + " "
    while rear != front:
        front += 1
        s = Q[front] # 队列首元素出队列
        for j in range(n):
            if p[s][j] == "1" and visited[j] == 0:
                res += names[j] + " "
                visited[j] = 1
                rear += 1
                Q.append(j)
    print(res.strip())


if __name__ == '__main__':
    N = int(input())
    for k in range(N):
        n,start = map(str, input().split())
        n = int(n)
        names = list(map(str, input().split())) # 节点名称数组，0..n-1
        p = [] # 邻接矩阵，0..n-1，0..n-1
        pDict = dict() # 节点名称字典，0..n-1 ，名称-行数
        for i in range(n):
            row = list(map(str, input().split()))
            pDict[row[0]] = i
            p.append(row[1:])
        BFS(pDict[start], n)
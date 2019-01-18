'''
距离问题
描述
In a given cartesian plane, there are N points. We need to find the Number of Pairs of points(A,B) such that
Point A and Point B do not coincide.
Manhattan Distance and the Euclidean Distance between the points should be equal.
Note : Pair of 2 points(A,B) is considered same as Pair of 2 points(B,A).
Manhattan Distance = |x2-x1|+|y2-y1|
Euclidean Distance = ((x2-x1)^2 + (y2-y1)^2)^0.5 where points are (x1,y1) and (x2,y2).
Constraints:1<=T <= 50, 1<=N <= 2*10 ^ 5, 0<=(|Xi|, |Yi|) <= 10^9
输入
First Line Consist of T - number of test cases.
For each Test case:First Line consist of N , Number of points.
Next line contains N pairs contains two integers Xi and Yi，i.e, X coordinate and the Y coordinate of a Point
输出
Print the number of pairs as asked above.
输入样例
1
2
1 1
7 5
输出样例
0
'''
def printPairs(p):
    res = []
    while len(p) != 0:
        A = p.pop()
        for B in p:
            if ManEqualEuc(A[0], A[1], B[0], B[1]):
                res.append([A, B])
    print(len(res))


def ManEqualEuc(x1, y1, x2, y2):
    # 计算曼哈顿距离
    Man = abs(x2 - x1) + abs(y2 - y1)
    # 计算欧几里得距离
    Euc = pow(pow(x2 - x1, 2) + pow(y2 - y1, 2), 0.5)
    return Man == Euc

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        N = int(input())
        points = []
        for n in range(N):
            a, b = map(int, input().split())
            points.append([a, b])
        printPairs(points)
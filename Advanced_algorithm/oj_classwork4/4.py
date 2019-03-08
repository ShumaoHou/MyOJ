"""
最小化初始点
描述
Given a grid with each cell consisting of positive, negative or no points i.e, zero points.
We can move across a cell only if we have positive points ( > 0 ).
Whenever we pass through a cell, points in that cell are added to our overall points.
We need to find minimum initial points to reach cell (m-1, n-1) from (0, 0) by following these certain set of rules :
1.From a cell (i, j) we can move to (i+1, j) or (i, j+1).
2.We cannot move from (i, j) if your overall points at (i, j) is <= 0.
3.We have to reach at (n-1, m-1) with minimum positive points i.e., > 0.
输入
The first line contains an integer 'T' denoting the total number of test cases.
In each test cases, the first line contains two integer 'R' and 'C' denoting the number of rows and column of array.
The second line contains the value of the array i.e the grid, in a single line separated by spaces in row major order.
Constraints:
1 ≤ T ≤ 30
1 ≤ R,C ≤ 10
-30 ≤ A[R][C] ≤ 30
Input: points[m][n] =
 -2, -3, 3},
{-5, -10, 1},
{10, 30, -5}
};
输出
Print the minimum initial points to reach the bottom right most cell in a separate line.
7
Explanation:
7 is the minimum value to reach destination with
positive throughout the path. Below is the path.
(0,0) -> (0,1) -> (0,2) -> (1, 2) -> (2, 2)
We start from (0, 0) with 7, we reach(0, 1)
with 5, (0, 2) with 2, (1, 2) with 5, (2, 2)with and finally we have 1 point (we needed
greater than 0 points at the end).
输入样例 1
1
3 3
-2 -3 3 -5 -10 1 10 30 -5
输出样例 1
7
"""


def minInitialPoints(points):
    """
    dp[i][j] represents the minimum initial
    points player should have so that when
    starts with cell(i, j) successfully
    reaches the destination cell(m-1, n-1)
    """
    dp = [[0 for x in range(C + 1)]
          for y in range(R + 1)]
    m, n = R, C

    if points[m - 1][n - 1] > 0:
        dp[m - 1][n - 1] = 1
    else:
        dp[m - 1][n - 1] = abs(points[m - 1][n - 1]) + 1
    ''' 
    Fill last row and last column as base 
    to fill entire table 
    '''
    for i in range(m - 2, -1, -1):
        dp[i][n - 1] = max(dp[i + 1][n - 1] -
                           points[i][n - 1], 1)
    for i in range(2, -1, -1):
        dp[m - 1][i] = max(dp[m - 1][i + 1] -
                           points[m - 1][i], 1)
    ''' 
    fill the table in bottom-up fashion 
    '''
    for i in range(m - 2, -1, -1):
        for j in range(n - 2, -1, -1):
            min_points_on_exit = min(dp[i + 1][j],
                                     dp[i][j + 1])
            dp[i][j] = max(min_points_on_exit -
                           points[i][j], 1)
    return dp[0][0]


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        R, C = map(int, input().split())
        arr = list(map(int, input().split()))
        # 初始化矩阵
        M = [[0 for c in range(C)] for r in range(R)]
        a = 0
        for r in range(R):
            for c in range(C):
                M[r][c] = arr[a]
                a += 1
        print(minInitialPoints(M))


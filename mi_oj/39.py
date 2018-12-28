'''
 寻找最大主对角线的和
任意给一个m*n矩阵(m>=2, n>=2)，元素均为非负数，
请找出其中主对角线和最大的二阶子矩阵，求出主对角线和。
（主对角线：一个n维矩阵的主对角线为所有第k行第k列元素的全体，k=1, 2, 3… n，即从左上到右下的一条斜线）
举例： 有一个3*5的矩阵如下：
3 3 1 3 4
5 5 7 10 1
2 9 5 3 3
其中，主对角线和最大的二阶子矩阵是: 5 5 2 9 可得出其主对角线和为14
输入一行 m*n (1 < m < 50, 1 < n < 50)个正整数，
每 m 个数用分号;分隔，表示矩阵行，每行内元素间用逗号,分隔。
 例如：3,3,1,3,4;5,5,7,10,1;2,9,5,3,3，表示矩阵： 3 3 1 3 4 5 5 7 10 1 2 9 5 3 3
输出：一个整数，表示最大的主对角线和
输入样例
3,3,1,3,4;5,5,7,10,1;2,9,5,3,3
输出样例
14
'''
"""
@param string line 为单行测试数据
@return string 处理后的结果
"""
def solution(line):
    cols = line.strip().split(";")
    matrix = []
    m = n = 0
    for col in cols:
        n = len(col.split(","))
        m += 1
        matrix.append(col.split(","))
    maxSum = 0
    for i in range(m - 1):
        for j in range(n - 1):
            sum = int(matrix[i][j]) + int(matrix[i + 1][j + 1])
            if sum > maxSum:
                maxSum = sum
    return str(maxSum)

print(solution(input()))
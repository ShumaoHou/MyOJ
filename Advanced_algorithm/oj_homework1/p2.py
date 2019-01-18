'''
子矩阵问题
给定一个矩形区域，每一个位置上都是1或0，求该矩阵中每一个位置上都是1的最大子矩形区域中的1的个数。
Input
输入的每一行是用空格隔开的0或1。
Output
输出一个数值。
Sample Input
1 0 1 1
1 1 1 1
1 1 1 0
Sample Output
6
'''
# 判断matrix矩阵是否有row行col列的全一子矩阵
def maxMatrix(matrix):
    # 矩阵行数
    H = len(matrix)
    if (H <= 0):
        return 0
    # 矩阵列数
    W = len(matrix[0])
    if (W <= 0):
        return 0
    # 初始化计数矩阵
    left = [[0]*W for i in range(H)]
    MaxArea = 0
    for i in range(H):
        for j in range(W):
            if matrix[i][j] == 0:
                left[i][j] = 0
            elif j == 0:
                left[i][j] = 1
            else:
                left[i][j] = left[i][j-1] + 1
    # 遍历计数矩阵，寻找最大子矩阵
    for i in range(H):
        for j in range(W):
            if (left[i][j] == 0):
                continue
            # 遍历当前非零元素的列上方
            k = i - 1
            area = left[i][j]
            while(k >= 0 and left[k][j] >= left[i][j]):
                k -= 1
                area += left[i][j]
            # 遍历当前非零元素的列下方
            k = i + 1
            while (k < H and left[k][j] >= left[i][j]):
                k += 1
                area += left[i][j]
            # 更新最大子矩阵的1数
            MaxArea = max(MaxArea, area);
    return MaxArea;

if __name__ == '__main__':
    matrix = [] # 矩阵
    max_row = 0 # 行数
    max_col = 0 # 列数
    try:
        while True:
            input_list = list(map(int, input().split()))
            matrix.append(input_list)
            max_row += 1
    except EOFError:
        pass
    # print(matrix[0][1])
    print(maxMatrix(matrix))
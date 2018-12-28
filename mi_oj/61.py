'''
找出矩阵中相同的行
给一个由 0 和 1 组成的矩阵，其中有两行相同，仅通过遍历找到相同的行。输出行数。
如：
1,0,0,1,0
0,1,1,0,0
1,0,0,1,0
0,0,1,1,0
0,1,0,0,0
输出重复的行号为 1 和 3（行号从1开始）
输入:一个字符串，表示由0和1组成的矩阵，使用;分隔行，使用,分隔每行内的元素。
矩阵必然存在且只有一对重复的行。
输出:使用,分隔的两个整数，表示重复的两行。
输入样例
1,0,0,1,0;0,1,1,0,0;1,0,0,1,0;0,0,1,1,0;0,1,0,0,0
输出样例
1,3
'''
"""
@param string line 为单行测试数据
@return string 处理后的结果
"""
def solution(line):
    cols = line.strip().split(";")
    matrix = []
    for col in cols:
        matrix.append(col.split(","))
    continueFlag = False
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            # 判断是否相同
            for k in range(len(matrix[j])):
                if matrix[i][k] != matrix[j][k]:
                    continueFlag = True
                    break
            if continueFlag:
                continueFlag = False
                continue
            else:
                return str(i + 1) + "," + str(j + 1)

print(solution(input()))
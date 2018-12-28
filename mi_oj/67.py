'''
开始报数
有 500 个小孩围成一圈，编号从 1 到 500，从第一个开始报数：1，2，3，1，2，3，1，2，3，……每次报到 3 的小孩退出。
问第 n 个被淘汰的小孩，在最开始 500 人里是的编号是几？
输入:正整数 N，表示要计算的为第 N 个淘汰的小孩的编号，0 < N <= 500
输出:第 N 个淘汰的小孩的编号
输入样例
1
2
206
311
输出样例
3
6
176
223
'''
"""
@param string line 为单行测试数据
@return string 处理后的结果
"""
def solution(line):
    N = int(line)
    order = [0] * 501
    count = 0   # 淘汰编号
    i = 1   # 相对计数
    j = 1   # 绝对计数
    while True:
        if j > 500:
            j = 1
        if order[j] == 0:
            if i % 3 == 0:
                count += 1
                order[j] = count
                if count == N:
                    return j
            i += 1
            j += 1
        else:
            j += 1
            continue

print(solution(input()))
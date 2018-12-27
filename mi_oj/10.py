'''
爬楼梯
描述
在你面前有一个n阶的楼梯，你一步只能上1阶或2阶。 请问计算出你可以采用多少种不同的方式爬完这个楼梯。
输入
一个正整数，表示这个楼梯一共有多少阶
输出
一个正整数，表示有多少种不同的方式爬完这个楼梯
输入样例
5
10
输出样例
8
89
'''
"""
@param string line 为单行测试数据
@return string 处理后的结果
"""
def solution(line):
    N = int(line)
    # if N == 1:
    #     return str(1)
    # elif N == 2:
    #     return str(2)
    # return str(int(solution(str(N - 1))) + int(solution(str(N - 2))))
    a = [1, 1]
    for i in range(2, N + 1):
        a.append(a[i - 1] + a[i - 2])
    return str(a[N])

print(solution(input()))

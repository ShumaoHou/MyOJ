'''
优秀数字
判断一个数字是否为优秀数字。优秀数字定义为，一个整数M(M>=0)，有2条规则：
规则1：存在一个正整数N(N>=0)，使得M=2^N+1；
规则2：存在一个正整数N(N>=0)，使得M=2^N-1；
若同时满足规则1和规则2，则输出Very Good
若满足规则1而不满足规则2，则输出Good
若不满足规则1而满足规则2，则输出Bad
若都不满足，则输出Normal
输入：一个整数M(M>=0)
输出：该数属于的类型
输入样例
3
5
7
8
输出样例
Very Good
Good
Bad
Normal
'''
"""
@param string line 为单行测试数据
@return string 处理后的结果
"""
def solution(line):
    M = int(line.strip())
    one = False
    two = False
    N = 0
    while pow(2, N) < M + 1:
        N += 1
    if M - 1 == pow(2, N - 1):
        one = True
    if M + 1 == pow(2, N):
        two = True
    if one and two:
        return "Very Good"
    elif M == 2 or one:
        return "Good"
    elif two:
        return "Bad"
    else:
        return "Normal"

print(solution(input()))
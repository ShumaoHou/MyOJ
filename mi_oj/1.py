'''
描述
和所有的 OJ 平台一样，第一题作为热身题，也是送分题：给出两个非负数 aa 和 bb，输出 a+ba+b 的结果。
输入
包含两个非负数 aa 和 bb，以空格分隔；aa 和 bb 保证小于 2^{32}
输出
你的输出是对一行数据处理的结果，也即 a+ba+b 的结果。
输入样例
233 666
输出样例
899
'''
def solution(line):
    a, b = line.strip().split()
    return str(int(a) + int(b))

print(solution(input()))
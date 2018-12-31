'''
解救我 mi
标签：栈
给定一个只包含小写字母的字符串，现在我 mi 被众友商品牌的字符串围困在其中，
需要我们将字符串中的 mi 全部移除然后输出，保证最后输出的字符串中没有 "mi"。
输入:一行数据包含一个字符串，长度 <= 100000，字符串仅包含小写字母。
输出:处理后的字符串
输入样例
huaweimivivo
chuizimmmiioppo
samsungmimiapple
输出样例
huaweivivo
chuizimoppo
samsungapple
'''
"""
@param string line 为单行测试数据
@return string 处理后的结果
"""
def solution(line):
    line = list(line)
    stack = []
    while len(line) > 0:
        if len(stack) == 0:
            stack.append(line.pop())
            continue
        if line[-1] == "m" and stack[-1] == "i":
            stack.pop()
            line.pop()
        else:
            stack.append(line.pop())
    stack.reverse()
    return "".join(stack)


print(solution(input()))
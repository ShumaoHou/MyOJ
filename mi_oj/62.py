'''
括号配对
我们知道，在逻辑表达式中广泛使用了括号，而括号都是层次化成对出现的。
也就是任意左括号都应该存在一个在同一逻辑层级的右括号作为对应。 现在我们有一些仅由括号组成的字符串序列，
保证每个字符为大括号”{”,”}”、中括号”[”,”]”和小括号”(”,”)”中的一种。 需要判断给定的的序列是否合法。
输入:一行仅由括号组成的字符串
输出:如果序列合法输出 1，否则输出 0
输入样例
[()]
({[])}
[()]{}
输出样例
1
0
1
小提示
栈的典型应用
'''
"""
@param string line 为单行测试数据
@return string 处理后的结果
"""
def solution(line):
    stack = []
    for i in range(len(line)):
        if line[i] == "(" or line[i] == "[" or line[i] == "{":
            stack.append(line[i])
        elif len(stack) == 0:
            return 0
        elif (line[i] == ")" and stack[-1] == "(") or (line[i] == "]" and stack[-1] == "[") or (line[i] == "}" and stack[-1] == "{"):
            stack.pop()
        else:
            return 0
    return 1

print(solution(input()))
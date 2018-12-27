'''
构建短字符串
描述
给定任意一个较短的子串，和另一个较长的字符串，
判断短的字符串是否能够由长字符串中的字符组合出来，且长串中的每个字符只能用一次。
输入
一行数据包括一个较短的字符串和一个较长的字符串，
用一个空格分隔，如： ab aab bb abc aa cccc uak areuok
输出
如果短的字符串可以由长字符串中的字符组合出来，
返回字符串 “true”，否则返回字符串 "false"，注意返回字符串类型而不是布尔型。
输入样例
a b
aa ab
aa aab
uak areuok
输出样例
false
false
true
true
'''
"""
@param string line 为单行测试数据
@return string 处理后的结果
"""
def solution(line):
    a, b = line.strip().split()
    res = "false"   # 注意：返回的是字符串“false”和“true”
    bDict = dict()
    for i in range(len(b)):
        if b[i] not in bDict.keys():
            bDict[b[i]] = 1
        else:
            bDict[b[i]] += 1
    for i in range(len(a)):
        if a[i] not in bDict.keys() or bDict[a[i]] <= 0:
            return res
        bDict[a[i]] -= 1
    res = "true"
    return res

print(solution(input()))
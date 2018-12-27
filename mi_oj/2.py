'''
找出单独出现的数字
给出N个数字。其中仅有一个数字出现过一次，其他数字均出现过两次，找出这个出现且只出现过一次的数字。要求时间和空间复杂度最小。
输入多个数字，每个数字以空格分开。数字数量 N < 20，输入数字的最大值小于 256.
输出内容为只出现过唯一一次的数字
输入样例
10 10 11 12 12 11 16
输出样例
16
'''
"""
@param string line 为单行测试数据
@return string 处理后的结果
"""
def solution(line):
    numList = list(map(int, line.strip().split()))
    numDict = dict()
    for i in range(len(numList)):
        if numList[i] not in numDict.keys():
            numDict[numList[i]] = 1
        else:
            numDict[numList[i]] += 1
    for key in numDict.keys():
        if numDict[key] == 1:
            return str(key)

print(solution(input()))
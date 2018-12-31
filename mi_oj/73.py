'''
找出单独出现的数字II
给出一个数组，数组中的数字皆为正整数，除了某一个数字，其他的数字都会出现三次。 找出那个只出现一次的数。
输入:3n+1的正整数数组，使用逗号(,)分隔(n>0)
输出:单独出现的数字
输入样例
2,3,2,2
5,1,4,5,4,5,4
输出样例
3
1
'''
"""
@param string line 为单行测试数据
@return string 处理后的结果
"""
def solution(line):
    numList = list(map(int, line.strip().split(",")))
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
'''
找数字对
有一串可能含重复数字的列表，例如 N = {4,13,5,6,35,85,3}，
对于任意 A ∈ N，B ∈ N, 使 A+B = 10 或 |A-B| = 10； 即两数之合为 10 或两数之差的绝对值为 10。
找出所有满足条件的数字对 {A,B} 的个数。(A, B的顺序与原始数组保持一致)
输入
一行文本由英文逗号分隔，如 6,4,16
输出
2
输入样例
4,13,5,6,35,85,3
13,3,6,8,12,4,45,56,66,16
6,4,16
输出样例
2
4
2
'''
"""
@param string line 为单行测试数据
@return string 处理后的结果
"""
def solution(line):
    numList = list(map(int, line.strip().split(",")))
    sum = 0
    for i in range(len(numList)):
        for j in range(i + 1, len(numList)):
            if numList[i] + numList[j] == 10 or abs(numList[i] - numList[j]) == 10:
                # print(str(i) + "_" + str(j))
                sum += 1
    return sum

print(solution(input()))
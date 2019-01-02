'''
第一个缺失正数
给出一个无序的数列，找出其中缺失的第一个正数，要求复杂度为 O(n)
如：[1,2,0]，第一个缺失为3。 如：[3,4,-1,1]，第一个缺失为2。
输入
1,2,0
输出
3
输入样例
1,2,0
3,4,-1,1
-1,-3,-5
1,2,3
-1,-10,0
输出样例
3
2
1
4
1

'''
"""
@param string line 为单行测试数据
@return string 处理后的结果
"""
def solution(line):
    numList = list(map(int, line.strip().split(",")))
    numList.sort()
    start = False
    num = 1
    for i in range(len(numList)):
        if numList[i] <= 0:
            continue
        elif not start:
            start = True
            num = numList[i]
        else:
            if num != numList[i]:
                return str(num)
        num += 1
    return str(num)

print(solution(input()))
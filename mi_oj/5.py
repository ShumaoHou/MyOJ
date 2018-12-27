'''
找出旋转有序数列的中间值

给出一个有序数列随机旋转之后的数列，如原有序数列为：[0,1,2,4,5,6,7] ，旋转之后为[4,5,6,7,0,1,2]。
假定数列中无重复元素，且数列长度为奇数。 求出旋转数列的中间值。如数列[4,5,6,7,0,1,2]的中间值为4。
输入
4,5,6,7,0,1,2
输出
4
输入样例
1
1,2,3
4,5,6,7,0,1,2
12,13,14,5,6,7,8,9,10
输出样例
1
2
4
9
'''
"""
@param string line 为单行测试数据
@return string 处理后的结果
"""
def solution(line):
    numList = list(map(int, line.strip().split(",")))
    numList.sort()
    return str(numList[int(len(numList) / 2)])

print(solution(input()))
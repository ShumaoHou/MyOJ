'''
找出可能的合的组合
给出一组不重复的正整数，从这组数中找出所有可能的组合使其加合等于一个目标正整数 M，如：
一组数为 1, 2, 3，目标数为 4，那么可能的加合组合为：
1, 1, 1, 1
1, 1, 2
1, 2, 1
1, 3
2, 1, 1
2, 2
3, 1
注意相同的组合数字顺序不同也算一种，所以这个例子的结果是 7 种。
输入：一组连续不重复的 N 个正整数（, 隔开，0<N<100）以及目标正整数（与数组之间用空格隔开）
输出：所有可能的加合等于目标正整数 M 的组合种数
输入样例
1,2,3 4
输出样例
7
'''
"""
@param string line 为单行测试数据
@return string 处理后的结果
"""
def achGoal (numList, goal):
    if goal == 0:
        return 1
    numList.sort()
    for i in range(len(numList)):
        if numList[i] > goal:
            numList = numList[0:i]
            break
    res = 0
    for i in range(len(numList)):
        res += achGoal(numList, goal - numList[i])
    return res

def solution(line):
    numStr, goal= map(str, line.strip().split())
    numList = list(map(int, numStr.strip().split(",")))
    goal = int(goal)
    return achGoal(numList, goal)

print(solution(input()))
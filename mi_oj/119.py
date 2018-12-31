'''
小米兔跳格子
米兔爸爸为了让小米兔好好锻炼身体，便给小米兔设置了一个挑战——跳格子。
要吃到自己心爱的胡萝卜，小米兔需要跳过面前一些格子。
现有 N个格子，每个格子内都写上了一个非负数，表示当前最多可以往前跳多少格，胡萝卜就放在最后一个格子上。
米兔开始站在第 1 个格子，试判断米兔能不能跳到最后一个格子吃到胡萝卜呢？
输入：输入为 N 个数字 (N <10)，用空格隔开，第 i 个数字 s_i( 0 <= s_i <10)
 表示米兔站在第 i 个格子上时，最多能往前跳的格数。
输出：若米兔能跳到最后一个格子上吃到胡萝卜，输出 “true“，否则输出 “false“
输入样例
2 0 1 0 0 3 4
输出样例
false
'''
"""
@param string line 为单行测试数据
@return string 处理后的结果
"""
def solution(line):
    numList = list(map(int, line.strip().split()))
    i = 0
    res = "false"
    while True:
        if i == len(numList) - 1:
            res = "true"
            break
        if numList[i] == 0 or i > len(numList) - 1:
            break
        i += numList[i]
    return res

print(solution(input()))
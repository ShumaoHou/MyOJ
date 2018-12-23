'''
子数组的取值范围
描述
给定数组arr和整数num，求arr的连续子数组中满足：其最大值减去最小值的结果大于num的个数。
请实现一个时间复杂度为O(length(arr))的算法。
输入
输入的第一行为数组，每一个数用空格隔开，第二行为num。
输出
输出一个值。
输入样例
3 6 4 3 2
2
输出样例
14
'''
# 计算满足条件的子数组数
def numOfSubArr(arr, num):
    count = 0  # 满足条件子数组数
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if (abs(arr[i] - arr[j]) > num):
                count += len(arr) - j
                break   # 一旦找到，则大于j的子数组都满足
    return count

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    num = int(input())
    print(numOfSubArr(arr, num))

'''
数组和窗口
给定一个整型数组arr和一个大小为w的窗口，窗口从数组最左边滑动到最右边，
每次向右滑动一个位置，求出每一次滑动时窗口内最大元素的和。
输入
输入的第一行为数组，每一个元素使用空格隔开；第二行为窗口大小。
输出
输出一个值。
输入样例
4 3 5 4 3 3 6 7
3
输出样例
32

AC情况包含初始位置
'''
arr = list(map(int, input().split()))   # 整型数组
w = int(input())    # 窗口大小
n = len(arr) - w +1     # 移动次数
sum = 0
for i in range(n):
    max = 0
    for j in range(w):
        if arr[i + j] > max :
            max = arr[i + j]
    sum += max
print(sum)
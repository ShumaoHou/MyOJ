'''
按数值个数排序
描述
Given an array of integers, sort the array according to frequency of elements.
For example, if the input array is {2, 3, 2, 4, 5, 12, 2, 3, 3, 3, 12}, then modify the array to {3, 3, 3, 3, 2, 2, 2, 12, 12, 4, 5}.
If frequencies of two elements are same, print them in increasing order.
输入
The first line of input contains an integer T denoting the number of test cases.
The description of T test cases follows.
The first line of each test case contains a single integer N denoting the size of array.
The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.（1 ≤ T ≤ 70；30 ≤ N ≤ 130；1 ≤ A [ i ] ≤ 60 ）
输出
Print each sorted array in a seperate line. For each array its numbers should be seperated by space.
输入样例
1
5
5 5 4 6 4
输出样例
4 4 5 5 6

设立计数数组
'''
def printArr(arr):
    arr.sort()
    d = [0] * max(arr)
    for i in range(len(arr)):
        d[arr[i] - 1] += 1
    res = []
    while max(d) != 0:
        maxCount = max(d)
        for i in range(len(d)):
            if d[i] == maxCount:
                appArr = [i + 1] * maxCount
                res.extend(appArr)
                d[i] = 0
                break
    resStr = ""
    for i in range(len(res)):
        resStr += str(res[i]) + " "
    print(resStr.strip())

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        printArr(A)
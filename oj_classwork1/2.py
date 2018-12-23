'''
最小交换次数
描述
Given an array of N distinct elementsA[ ], find the minimum number of swaps required to sort the array.
Your are required to complete the function which returns an integer denoting the minimum number of swaps, required to sort the array.
输入
The first line of input contains an integer T denoting the no of test cases . Then T test cases follow .
Each test case contains an integer N denoting the no of element of the array A[ ].
In the next line are N space separated values of the array A[ ] .(1<=T<=100;1<=N<=100;1<=A[] <=1000)
输出
For each test case in a new line output will be an integer denoting minimum umber of swaps that are required to sort the array.
输入样例
2
4
4 3 2 1
5
1 5 4 3 2
输出样例
2
2
'''
def swap(A):
    B = A.copy()
    B.sort()
    loops = 0
    flag = [False] * len(A)
    for i in range(len(A)):
        if not flag[i]:
            j = i
            while(not flag[j]):
                flag[j] = True
                j = B.index(A[j])
            loops += 1
    return len(A) - loops
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        print(swap(A))
'''
Searching_4
描述
Given n Magnets which are placed linearly,
with each magnet to be considered as of point object.
Each magnet suffers force from its left sided magnets such that they repel it to the right and vice versa.
All forces are repulsive. The force being equal to the distance (1/d , d being the distance).
Now given the positions of the magnets, the task to find all the points along the linear line where net force is ZERO.
现在给出磁体的位置，沿着直线找到所有磁力是零的点。
Note: Distance have to be calculated with precision of 0.0000000000001.
Constraints:1<=T<=100,1<=N<=100,1<=M[]<=1000
输入
The first line of input contains an integer T denoting the no of test cases.
Then T test cases follow.
The second line of each test case contains an integer N.
Then in the next line are N space separated values of the array M[],denoting the positions of the magnet.
输出
For each test case in a new line print the space separated points having net force zero till precised two decimal places.
输入样例
2
2
1 2
4
0 10 20 30
输出样例
1.50
3.82 15.00 26.18
'''
'''
非递归AC
'''
def zeroPoints(i, arr, size):
    low = arr[i]
    high = arr[i + 1]
    while low < high:
        mid = low + (high - low) / 2
        r = 0
        for j in range(size):
            if j <= i:
                r = r + 1 / (mid - arr[j])
            else:
                r = r + 1 / (mid - arr[j])
        if r <= 0.000000000001 and r >= 0:
            return mid
        elif r>0.000000000001:
            low = mid
        else:
            high = mid
    return 0


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N = int(input())
        M = list(map(int, input().split()))
        for i in range(N - 1):
            if i == N - 2:
                print('%.2f' % zeroPoints(i, M, N))
            else:
                print('%.2f' % zeroPoints(i, M, N), end=" ")

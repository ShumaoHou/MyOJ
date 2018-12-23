'''
2
4
4 3 2 1
5
1 5 4 3 2

2
2
'''

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        # 记录最终位置
        B = A.copy()
        B.sort()
        count = 0
        for i in range(len(A)):
            if A[i] != B[i]:
                index = B.index(A[i])
                A[i], A[index] = A[index], A[i]
                count += 1
        print(count)
'''
1
8
8 3 2 9 7 1 5 4

17
'''
def mergeSort(arrA):
    num = 0
    if len(arrA) > 1:
        arrB = arrA[0: int(len(arrA) / 2)]
        arrC = arrA[int(len(arrA) / 2): len(arrA)]
        num += mergeSort(arrB)
        num += mergeSort(arrC)
        num += merge(arrB, arrC, arrA)
    return num

def merge(B, C, A):
    i, j, k, num = 0, 0, 0, 0
    while i < len(B) and j < len(C):
        if B[i] <= C[j]:
            A[k] = B[i]
            i += 1
        else:
            A[k] = C[j]
            j += 1
            num += 1
        k += 1
    if i == len(B):
        for m in range(j, len(C)):
            A[k] = C[m]
            k += 1
    else:
        for m in range(i, len(B)):
            A[k] = B[m]
            k += 1
    return num
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        print(mergeSort(A))
        print(A)
def DoubleEndLIS(arr):
    resArr = []
    arrLen = len(arr)
    LIS = [0] * arrLen
    L2R = [0] * arrLen
    # 从左到右
    LIS[0] = arr[0]
    for i in range(arrLen):
        low, high = 0, L2R[i - 1]
        while low <= high:
            mid = int((low + high) / 2)
            if LIS[mid] < arr[i]:
                low = mid + 1
            else:
                high = mid - 1
        LIS[low] = arr[i]
        if low > L2R[i - 1]:
            L2R[i] = L2R[i - 1] + 1
        else:
            L2R[i] = L2R[i - 1]
    for i in range(arrLen):
        L2R[i] += 1
    # 从右到左
    LIS = [0] * arrLen
    R2L = [0] * arrLen
    k = 0
    LIS[0] = arr[arrLen - 1]
    for j in range(arrLen - 1):
        i = arrLen - 2 - j
        low, high = 0, R2L[k]
        while low <= high:
            mid = int((low + high) / 2)
            if LIS[mid] < arr[i]:
                low = mid + 1
            else:
                high = mid - 1
        LIS[low] = arr[i]
        if low > R2L[k]:
            R2L[k + 1] = R2L[k] + 1
        else:
            R2L[k + 1] = R2L[k]
        k += 1
    for i in range(k):
        R2L[i] += 1
    maxLen = 0
    for i in range(arrLen):
        # print(i)

        if L2R[i] + R2L[arrLen - i - 1] > maxLen:
            maxLen = L2R[i] + R2L[arrLen - i - 1]
            print(L2R[i])
            print(R2L[arrLen - i - 1])
    print(maxLen)


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    DoubleEndLIS(arr)

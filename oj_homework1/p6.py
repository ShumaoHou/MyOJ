'''
固定和的元素对
描述
输入一个数组和一个数字，在数组中查找两个数，使得它们的和正好是输入的那个数字，统计这样两个数的对数。
输入
输入第一行是数组，每一个数用空格隔开；第二行是数字和。
输出
输出这样两个数有几对。
输入样例
1 2 4 7 11 0 9 15
11
输出样例
3
'''
if __name__ == '__main__':
    arr = list(map(int, input().split()))
    num = int(input())
    pairs = 0
    arr.sort()
    l = len(arr)
    for i in range(l):
        a = arr[i]
        j = i + 1
        while(j < l):
            if (a + arr[j] == num):
                pairs += 1
            elif (a + arr[j] > num):
                break
            j += 1
    print(pairs)

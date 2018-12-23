'''
区间第k最小
描述
找到给定数组的给定区间内的倒数第K小的数值。
输入的第一行为数组，每一个数用空格隔开；
第二行是区间（第几个数到第几个数，两头均包含），两个值用空格隔开；
第三行为K值。
输入样例
1 2 3 4 5 6 7
3 5
2
输出样例
4
'''
if __name__ == '__main__':
    arr = list(map(int, input().split()))
    min,max = map(int, input().split())
    K = int(input())
    arrK = []
    for i in range(max - min + 1):
        arrK.append(arr[i + min - 1])
    arrK.sort() # 排序
    print(arrK[K - 1])
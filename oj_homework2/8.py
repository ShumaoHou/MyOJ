'''
非递归合并排序
合并（归并）排序的核心思想是：每次从中间位置将数组分组再分别排序。请实现其非递归方案。
输入的每一行表示一个元素为正整数的数组，所有值用空格隔开，第一个值为数值长度，其余为数组元素值。
输出的每一行为排序结果，用空格隔开，末尾不要空格。
输入样例
13 24 3 56 34 3 78 12 29 49 84 51 9 100
输出样例
3 3 9 12 24 29 34 49 51 56 78 84 100
'''
'''
代码出处：
https://www.jianshu.com/p/3f27384387c1
'''
def merge(seq,low,mid,height):
    """合并两个已排序好的列表，产生一个新的已排序好的列表"""
    # 通过low,mid height 将[low:mid) [mid:height)提取出来
    left = seq[low:mid]
    right = seq[mid:height]
    k = 0   #left的下标
    j = 0   #right的下标
    result = [] #保存本次排序好的内容
    #将最小的元素依次添加到result数组中
    while k < len(left) and j < len(right):
        if left[k] <= right[j]:
            result.append(left[k])
            k += 1
        else:
            result.append(right[j])
            j += 1
    #将对比完后剩余的数组内容 添加到已排序好数组中
    result += left[k:]
    result += right[j:]
    #将原始数组中[low:height)区间 替换为已经排序好的数组
    seq[low:height] = result

if __name__ == '__main__':
    try:
        while True:
            inputList = list(map(int, input().split()))
            N = inputList[0]
            orderList = inputList[1:]
            i = 1   # 子数组的大小
            while i < len(orderList):
                low = 0
                while low < len(orderList):
                    mid = low + i
                    height = min(low + 2 * i, len(orderList))
                    if mid < height:
                        merge(orderList, low, mid, height)
                    low += 2 * i
                i *= 2
            res = ""
            for i in range(N):
                res += str(orderList[i]) + " "
            print(res.strip())
    except EOFError:
        pass
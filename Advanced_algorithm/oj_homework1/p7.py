'''
先升后降
描述: 从一列数中筛除尽可能少的数使得从左往右看，这些数是从小到大再从大到小的。
输入: 输入时一个数组，数值通过空格隔开。
输出: 输出筛选之后的数组，用空格隔开。如果有多种解雇哦，则一行一种结果。
输入样例
1 2 4 7 11 10 9 15 3 5 8 6
输出样例
1 2 4 7 11 10 9 8 6
'''
def fun_LIS(arr):
    arrLen = len(arr)
    count = [1] * arrLen  # 以第i元素结尾的LIS长度
    id = [0] * arrLen  # 记录第i元素在LIS第i-1元素的位置
    for i in range(arrLen):
        for j in range(i):
            if arr[j] < arr[i] and count[j] + 1 > count[i]:
                count[i] = count[j] + 1
                id[i] = j
    LIS_len = max(count)  # LIS长度
    id_LIS = count.index(LIS_len)   # LIS尾元素坐标
    # 根据id，向前追溯，生成LIS列表
    LIS_list = []
    LIS_list.append(arr[id_LIS])
    for i in range(LIS_len - 1):
        id_next = id[id_LIS]
        LIS_list.append(arr[id_next])
        id_LIS = id_next
    LIS_list.reverse()
    return LIS_len, LIS_list

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    LIS_sum = []  # 每个i上前后LIS的总长度
    asc = []    # 前LIS
    desc = []   # 后LIS
    for i in range(len(arr)):
        arr1 = arr[:i + 1]
        asc_len, asc_list = fun_LIS(arr1)  # 0-i的LIS
        arr2 = arr[i:len(arr)]
        arr2.reverse()
        desc_len, desc_list = fun_LIS(arr2)  # i-len的LIS
        LIS_sum.append(asc_len + desc_len - 1)  # 去掉多余i的长度
        asc.append(asc_list)
        desc.append(desc_list)
    # 连接正反LIS
    LIS_sum_max = max(LIS_sum)
    for i in range(len(LIS_sum)):
        if LIS_sum[i] == LIS_sum_max:
            asc_list = asc[i]
            desc_list = desc[i]
            desc_list.reverse()
            if asc_list[-1] == desc_list[0]:
                asc_list.extend(desc_list[1:])
            else:
                asc_list.extend(desc_list)
            s = ''
            for i in range(len(asc_list)):
                s += str(asc_list[i])
                s += ' '
            print(s.strip())
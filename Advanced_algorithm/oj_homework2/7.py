'''
非递归快排
快速排序的核心思想是使用元素的值对数组进行划分。实现其非递归方案。
输入的每一行表示一个元素为正整数的数组，所有值用空格隔开，第一个值为数值长度，其余为数组元素值。
输出的每一行为排序结果，用空格隔开，末尾不要空格。
输入样例
13 24 3 56 34 3 78 12 29 49 84 51 9 100
输出样例
3 3 9 12 24 29 34 49 51 56 78 84 100
'''
'''
代码出处：
https://blog.csdn.net/u014204761/article/details/80536940
'''
def quick_sort_other(array, l, r):
    '''
    算法导论里的思想
    i表示[l,i]都比pivot小
    j依次遍历元素
    '''
    if l >= r:
        return
    stack = [l,r]
    while stack:
        low = stack.pop(0)
        high = stack.pop(0)
        if high <= low:
            continue
        pivot = array[high]
        i = low - 1 ###初始值是-1
        for j in range(low,high+1):
            ###如果小于pivot， 则交换，交换的目的是保证[l,i]都比pivot小
            if array[j] <= pivot:
                i += 1
                t = array[i]
                array[i] = array[j]
                array[j] = t
        stack.extend([low, i-1, i + 1, high])
    return array

if __name__ == '__main__':
    try:
        while True:
            inputList = list(map(int, input().split()))
            N = inputList[0]
            orderList = inputList[1:]
            orderList = quick_sort_other(orderList, 0, N - 1)
            res = ""
            for i in range(N):
                res += str(orderList[i]) + " "
            print(res.strip())
    except EOFError:
        pass
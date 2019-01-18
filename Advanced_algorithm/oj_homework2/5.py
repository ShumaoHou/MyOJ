'''
冒泡排序
输入的每一行表示一个元素为正整数的数组，所有值用空格隔开，第一个值为数值长度，其余为数组元素值。
输出的每一行为排序结果，用空格隔开，末尾不要空格。
输入样例
13 24 3 56 34 3 78 12 29 49 84 51 9 100
输出样例
3 3 9 12 24 29 34 49 51 56 78 84 100
'''

if __name__ == '__main__':
    try:
        while True:
            inputList = list(map(int, input().split()))
            N = inputList[0]
            orderList = inputList[1:]
            for i in range(len(orderList) - 1): # 最多len - 1次遍历
                for j in range(len(orderList) - i - 1):
                    if orderList[j] > orderList[j + 1]:
                        orderList[j], orderList[j + 1] = orderList[j + 1], orderList[j]
            res = ""
            for i in range(len(orderList)):
                res += str(orderList[i]) + " "
            print(res.strip())
    except EOFError:
        pass
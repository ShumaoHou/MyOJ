'''
插入排序
实现插入排序。
输入的每一行代表一个数组，其中的值用空格隔开，第一个值表示数组的长度。
输出排序的数组，用空格隔开，末尾不要空格。
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
            numList = inputList[1:] # 原始数组
            orderList = []
            orderList.append(numList[0])   # 排序好的数组
            for i in range(1, len(numList)):
                for j in range(len(orderList)):
                    if orderList[j] > numList[i]:
                        orderList.insert(j, numList[i])
                        break
                    elif j == len(orderList) - 1:
                        orderList.append(numList[i])
            res = ""
            for i in range(len(orderList)):
                res += str(orderList[i]) + " "
            print(res.strip())
    except EOFError:
        pass
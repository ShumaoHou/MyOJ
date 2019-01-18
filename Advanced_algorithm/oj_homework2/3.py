'''
链表区间逆序
将单个链表的每K个节点之间逆序，打印出新链表；最后不足K的节点数不需要逆序；要求时间复杂度为O(n)，额外空间复杂度为O(1)。
输入的每一行的值用空格隔开，第一个表示链表长度，中间为节点值，最后代表K。
输出的每一行为新的链表，节点值用空格隔开，末尾不要空格。
输入样例
8 1 2 3 4 5 6 7 8 3
8 a b c d e f g h 4
输出样例
3 2 1 6 5 4 7 8
d c b a h g f e
'''
class Node:
    '''
    定义节点类
    data:数据
    _next:下一个数据
    '''
    def __init__(self,data):
        self.data = data
        self._next = None
    def setNext(self, _next):
        self._next = _next
    def getNext(self):
        return self._next
    def getData(self):
        return self.data
# 将list链表反转，并返回反转后的list
def desc(list):
    res = None
    while list.getNext() != None:
        next = list.getNext()
        list.setNext(res)
        res = list
        list = next
    list.setNext(res)
    return list
# 连接两个链表
def connect(res, list):
    root = res
    while res.getNext() != None:
        res = res.getNext()
    res.setNext(list)
    return root

def printDesc(strList, N, K):
    # 构建单向链表
    root = node = Node(0)   # 头结点
    for i in range(N):
        newNode = Node(strList[i])
        node.setNext(newNode)
        node = newNode
    root = root.getNext()
    newNode = node = root
    res = Node(0)
    for i in range(1, N + 1):
        if i % K == 0:
            root = node.getNext()
            node.setNext(None)
            newNode = desc(newNode)
            res = connect(res, newNode)
            newNode = node = root
        else:
            node = node.getNext()
    # 如果N % K != 0，则会有不逆序的部分，将其连接
    if newNode != None:
        res = connect(res, newNode)
    resStr = ""
    res = res.getNext()
    while res != None:
        resStr += str(res.getData()) + " "
        res = res.getNext()
    print(resStr.strip())

if __name__ == '__main__':
    try:
        while True:
            inputList = list(map(str, input().split()))
            N = int(inputList[0])
            K = int(inputList[-1])
            strList = inputList[1:len(inputList) - 1]
            printDesc(strList, N, K)
    except EOFError:
        pass
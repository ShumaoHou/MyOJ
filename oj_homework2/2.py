'''
链表回文
判断一个单向链表是否为回文结构。自定义链表数据结构，要求时间复杂度为O(n)，额外空间复杂度为O(1)。
输入的每一行的值用空格隔开，第一个值为节点个数，后面为每一个节点值
输出:是回文则输出true，不是则输出false，一行表示一个链表的结果。
输入样例
3 1 2 1
4 1 2 2 1
3 3 5 3
6 a b c d c a
输出样例
true
true
true
false
'''
'''
第一次遍历：获取链表长度（这里在输入的时候就能知道）
第二次遍历：遍历到中间，并逆置前段列表
第三次遍历：从中间到两端进行比较
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

def isPalindrome(strList):
    # 构建单向链表
    p1 = p2 = node = Node(0)   # 头结点
    p3 = None
    length = len(strList)
    for i in range(length):
        newNode = Node(strList[i])
        node.setNext(newNode)
        node = newNode
    p2 = p2.getNext()
    # 遍历到中间，并逆置
    for i in range(int(length / 2)):
        p1 = p2.getNext()
        p2.setNext(p3)
        p3 = p2
        p2 = p1
    if length % 2 == 1:
        p1 = p1.getNext()
    # 从中间到两端进行比较
    while p1 != None and p3 != None:
        if p1.getData() != p3.getData():
            return False
        p1 = p1.getNext()
        p3 = p3.getNext()
    return True
if __name__ == '__main__':
    try:
        while True:
            inputList = list(map(str, input().split()))
            N = inputList[0]
            strList = inputList[1:]
            # OJ结果和python的bool差别在于是否首字母大小写
            if isPalindrome(strList):
                print("true")
            else:
                print("false")
    except EOFError:
        pass

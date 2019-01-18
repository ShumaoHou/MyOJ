'''
汉诺塔
描述
汉诺塔问题中限制不能将一层塔直接从最左侧移动到最右侧，也不能直接从最右侧移动到最左侧，
而是必须经过中间。求当有N层塔的时候移动步数。
输入
输入的第一行为N。
输出
移动步数。
输入样例
2
输出样例
8

递归实现
'''
times = 0
# 将a柱上的塔移动b柱上
def move(a, b):
    # print(a + "-->" + b)
    global times
    times += 1
# 汉诺塔递归
def Hanoi(n, a, b, c):
    if(1 == n): # 只有一层塔，a->b->c
        move(a, b)
        move(b, c)
    else:
        Hanoi(n - 1, a, b, c)   # 
        move(a, b)
        Hanoi(n - 1, c, b, a)
        move(b, c)
        Hanoi(n - 1, a, b, c)
if __name__ == '__main__':
    n = int(input())
    a = 'a'
    b = 'b'
    c = 'c'
    Hanoi(n, a, b, c)
    print(times)
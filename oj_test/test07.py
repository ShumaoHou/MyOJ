'''
A+B for Input-Output Practice (VII)
描述
Your task is to Calculate a + b.
输入
The input will consist of a series of pairs of integers a and b, separated by a space, one pair of integers per line.
输出
For each pair of input integers a and b you should output the sum of a and b, and followed by a blank line.
输入样例
1 5
10 20
输出样例
6

30
'''
try:
    while True:
        a, b = map(int, input().split(" "))
        print(a + b)
        print()
except EOFError:
    pass
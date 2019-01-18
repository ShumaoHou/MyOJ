'''
A+B for Input-Output Practice (I)
描述
our task is to Calculate a + b. Too easy?!
Of course! I specially designed the problem for acm beginners.
You must have found that some problems have the same titles with this one, yes, all these problems were designed for the same aim
输入
The input will consist of a series of pairs of integers a and b, separated by a space, one pair of integers per line.
输出
For each pair of input integers a and b you should output the sum of a and b in one line,
and with one line of output for each line in input.
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
except EOFError:
    pass

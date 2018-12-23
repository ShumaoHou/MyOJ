'''
A+B for Input-Output Practice (II)
描述
The first line integer means the number of input integer a and b. Your task is to Calculate a + b.
输入
Your task is to Calculate a + b. The first line integer means the numbers of pairs of input integers.
输出
For each pair of input integers a and b you should output the sum of a and b in one line,
and with one line of output for each line in input.
输入样例
2
1 5
10 20
输出样例
6
30
'''
n = int(input())
for i in range(n):
    a, b = map(int, input().split(" "))
    print(a + b)
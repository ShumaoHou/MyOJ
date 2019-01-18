'''
A+B for Input-Output Practice (VI)
描述
Your task is to calculate the sum of some integers.
输入
Input contains multiple test cases, and one case one line.
Each case starts with an integer N, and then N integers follow in the same line.
输出
For each test case you should output the sum of N integers in one line,
and with one line of output for each line in input.
输入样例
4 1 2 3 4
5 1 2 3 4 5
输出样例
10
15
'''
try:
    while True:
        input_list = list(map(int, input().split()))
        M = input_list[0]
        sum = 0
        for m in range(M):
            sum = sum + input_list[m + 1]
        print(sum)
except EOFError:
    pass
'''
A+B for Input-Output Practice (III)
描述
Your task is to Calculate a + b.
输入
nput contains multiple test cases. Each test case contains a pair of integers a and b, one pair of integers per line.
A test case containing 0 0 terminates the input and this test case is not to be processed.
输出
For each pair of input integers a and b you should output the sum of a and b in one line,
and with one line of output for each line in input.
输入样例
1 5
10 20
0 0
输出样例
6
30
'''
a, b = map(int, input().split(" "))
while(not(a == 0 and b == 0)):
    # if (a == 0 and b == 0):
    #     break
    print(a + b)
    a, b = map(int, input().split(" "))
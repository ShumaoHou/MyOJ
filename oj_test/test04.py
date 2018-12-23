'''
A+B for Input-Output Practice (IV)
描述
Your task is to Calculate the sum of some integers.
输入
Input contains multiple test cases. Each test case contains a integer N,
and then N integers follow in the same line.
A test case starting with 0 terminates the input and this test case is not to be processed.
输出
For each group of input integers you should output their sum in one line,
and with one line of output for each line in input.
输入样例
4 1 2 3 4
5 1 2 3 4 5
0
输出样例
10
15
'''
while(True):
    input_list = list(map(int, input().split()))
    # split()默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
    # 使用split(" ") 报RE
    n = input_list[0]
    if n == 0:
        break
    sum = 0
    for i in range(n):
        sum = sum + input_list[i + 1]
    print(sum)
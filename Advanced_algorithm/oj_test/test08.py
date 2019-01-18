'''
A+B for Input-Output Practice(VIII)
描述
Your task is to calculate the sum of some integers
输入
Input contains an integer N in the first line, and then N lines follow.
Each line starts with a integer M, and then M integers follow in the same line
输出
For each group of input integers you should output their sum in one line,
and you must note that there is a blank line between outputs.
输入样例
3
4 1 2 3 4
5 1 2 3 4 5
3 1 2 3
输出样例
10

15

6
'''
N = int(input())
for n in range(N):
    input_list = list(map(int, input().split()))
    # split()默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
    # 使用split(" ") 报RE
    M = input_list[0]
    sum = 0
    for m in range(M):
        sum = sum + input_list[m + 1]
    print(sum)
    print()
'''
进制转换
给出一个P进制整数N，求N的Q进制表示 (0 <= N <= 32767， 2 <= P <= 16, 2 <= Q <= 16)
(0≤N≤32767，2≤P≤16,2≤Q≤16)。 大于 9 的数字依次使用小写字母 a、b、c、d、e、f 表示。
请勿使用已存在的进制转换库或函数，比如PHP中的base_convert()等。
输入:输入3个数，以空格分隔： 第1个数是待转换的数， 第2个数是待转换的数的进制， 第3个数是转换后的数的进制。
输出:输入转换后的数
输入样例
31 10 16
输出样例
1f
'''
"""
@param string line 为单行测试数据
@return string 处理后的结果
"""
def solution(line):
    N, P, Q = map(str, line.strip().split())
    P = int(P)
    Q = int(Q)
    # 先转换成10进制
    numTo10 = 0
    for i in range(len(N)):
        k = len(N) - i - 1
        base = pow(P, k)
        if N[i] == "a":
            base *= 10
        elif N[i] == "b":
            base *= 11
        elif N[i] == "c":
            base *= 12
        elif N[i] == "d":
            base *= 13
        elif N[i] == "e":
            base *= 14
        elif N[i] == "f":
            base *= 15
        else:
            base *= int(N[i])
        numTo10 += base
    # 10进制转换成Q进制
    toNum = ""
    q = numTo10
    while q != 0:
        r = q % Q
        if r == 10:
            r = "a"
        elif r == 11:
            r = "b"
        elif r == 12:
            r = "c"
        elif r == 13:
            r = "d"
        elif r == 14:
            r = "e"
        elif r == 15:
            r = "f"
        toNum = str(r) + toNum
        q = int(q / Q)
    return toNum

print(solution(input()))
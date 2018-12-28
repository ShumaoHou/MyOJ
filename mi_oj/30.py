'''
反向位整数
输入32位无符号整数，输出它的反向位。 例，输入4626149（以二进制表示为00000000010001101001011011100101），
返回2808701440（以二进制表示为10100111011010010110001000000000）。
输入：一个无符号32位整数字符串
输出：一个无符号32位整数，为输入整数的反向位
输入样例
4626149
输出样例
2808701440
'''
"""
@param string line 为单行测试数据
@return string 处理后的结果
"""
def solution(line):
    num = int(line.strip())
    numStr = ""
    while num != 0:
        numStr += str(num % 2)
        num = int(num / 2)
    while len(numStr) < 32:
        numStr += "0"
    two = 1
    num = 0
    for i in range(32):
        k = 31 - i
        num += int(numStr[k]) * two
        two *= 2
    return str(num)

print(solution(input()))
'''
最长公共子序列
描述
给定两个字符串，返回两个字符串的最长公共子序列（不是最长公共子字符串），可能是多个。
输入
输入为两行，一行一个字符串
输出
输出如果有多个则分为多行，先后顺序不影响判断。
输入样例
1A2BD3G4H56JK
23EFG4I5J6K7
输出样例
23G456K
23G45JK
'''
'''
d为方向矩阵
1：上
2：左上
3：左
4：左or上
'''
def LCS (a, b):
    C = [[0 for i in range(len(b) + 1)] for i in range(len(a) + 1)] # 定义矩阵C保存最长公共子序列长度
    d = [[0 for i in range(len(b) + 1)] for i in range(len(a) + 1)]  # 定义矩阵path保存最长公共子序列查找方向
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                C[i][j] = C[i - 1][j - 1] + 1
                d[i][j] = 1 # 左上
            elif C[i][j - 1] < C[i - 1][j]:
                C[i][j] = C[i - 1][j]
                d[i][j] = 2 # 上
            elif C[i][j - 1] > C[i - 1][j]:
                C[i][j] = C[i][j - 1]
                d[i][j] = 3 # 左
            else:   # C[i][j - 1] == C[i - 1][j]
                C[i][j] = C[i - 1][j]
                d[i][j] = 4 # 左or上
    maxLen = C[len(a)][len(b)]
    lcs = ""
    printLCS(d, a, lcs, 1, maxLen, len(a), len(b))

def printLCS (d, a, s, curLen, maxLen, i, j):
    if i == 0  or j == 0:
        return None
    dir = d[i][j]
    if dir == 1:
        if curLen == maxLen:
            s += a[i - 1]
            s = s[::-1]
            strDict[s] = i - 1
        elif curLen < maxLen:
            s += a[i - 1]
            printLCS(d, a, s, curLen + 1, maxLen, i - 1, j - 1)
    elif dir == 2:
        printLCS(d, a, s, curLen, maxLen, i - 1, j)
    elif dir == 3:
        printLCS(d, a, s, curLen, maxLen, i, j - 1)
    elif dir == 4:
        printLCS(d, a, s, curLen, maxLen, i - 1, j)
        printLCS(d, a, s, curLen, maxLen, i, j - 1)

if __name__ == '__main__':
    a = input().strip()
    b = input().strip()
    strDict = dict()
    LCS(a, b)
    for key in strDict.keys():
        print(key)

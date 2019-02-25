'''
棋盘覆盖问题：
给定一个大小为2^n * 2^n个小方格的棋盘，其中有一个位置已经被填充，
现在要用一个L型（2 * 2个小方格组成的大方格中去掉其中一个小方格）形状去覆盖剩下的小方格。
求出覆盖方案，即哪些坐标下的小方格使用同一个L型格子覆盖。注意：坐标从0开始。
左上方的第一个格子坐标为(0,0)，第一行第二个坐标为(0,1)，第二行第一个为(1,0)，以此类推。

输入: 第一行为测试用例个数，后面每一个用例有两行，
第一行为n值和特殊的格子的坐标（用空格隔开），
第二行为需要查找其属于同一个L型格子的格子坐标。

输出: 每一行为一个用例的解，先按照行值从小到大、
再按照列值从小到大的顺序输出每一个用例的两个坐标；用逗号隔开。
输入样例
1
1 1 1
0 0
输出样例
0 1,1 0
'''
'''
将2^k * 2^k问题分为4个规模为2^(k-1) * 2^(k-1)的子问题
'''
def chess(tr, tc, dr, dc, size, arr):
    if size == 1:
        return
    global num
    num += 1
    t = num
    s = int(size / 2)
    # 左上
    if (dr < tr + s and dc < tc + s):   #特殊点在左上方
        chess(tr, tc, dr, dc, s, arr)
    else: # 将右下角涂t
        arr[tr + s - 1][tc + s - 1] = t
        chess(tr, tc, tr + s - 1, tc + s - 1, s, arr)
    # 右上
    if (dr < tr + s and dc >= tc + s):   #特殊点在右上方
        chess(tr, tc + s, dr, dc, s, arr)
    else: # 将左下角涂t
        arr[tr + s - 1][tc + s] = t
        chess(tr, tc + s, tr + s - 1, tc + s, s, arr)
    # 左下
    if (dr >= tr + s and dc < tc + s):   #特殊点在左下方
        chess(tr + s, tc, dr, dc, s, arr)
    else: # 将右上角涂t
        arr[tr + s][tc + s - 1] = t
        chess(tr + s, tc, tr + s, tc + s - 1, s, arr)
    # 右下
    if (dr >= tr + s and dc >= tc + s):   #特殊点在右下方
        chess(tr + s, tc + s, dr, dc, s, arr)
    else: # 将左上角涂t
        arr[tr + s][tc + s] = t
        chess(tr + s, tc + s, tr + s, tc + s, s, arr)


if __name__ == '__main__':
    N = int(input())
    for k in range(N):
        inputList = list(map(int, input().split()))
        N = inputList[0]
        s_node = inputList[1:] # 特殊格子坐标
        f_node = list(map(int, input().split())) # 查找格子坐标
        size = pow(2, N)
        num = 0
        arr = [[0 for col in range(size)] for row in range(size)]
        chess(0, 0, s_node[0], s_node[1], size, arr)
        count = 0
        res = ""
        for i in range(size):
            for j in range(size):
                if arr[i][j] == arr[f_node[0]][f_node[1]]:
                    if not (i == f_node[0] and j ==f_node[1]):
                        if count == 0:
                            res += str(i) + " " + str(j) + ","
                        elif count == 1:
                            res += str(i) + " " + str(j)
                        count += 1
        print(res)
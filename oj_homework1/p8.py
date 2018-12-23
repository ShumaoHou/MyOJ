'''
调整数组使差最小
描述: 有两个序列 a,b，大小都为 n,序列元素的值任意整数，无序；
要求：通过交换 a,b 中的元素，使[序列 a 元素的和]与[序列 b 元素的和]之间的差最小。
输入: 输入为两行，分别为两个数组，每个值用空格隔开。
输出: 输出变化之后的两个数组内元素和的差绝对值。
输入样例
100 99 98 1 2 3
1 2 3 4 5 40
输出样例
96
'''
if __name__ == '__main__':
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    sumA = sum(a)
    sumB = sum(b)
    diff = sumA - sumB
    while abs(diff) > 0:
        new_diff = 0
        ai, bj = 0, 0
        for i in range(len(a)):
            for j in range(len(b)):
                '''关键是判断交换后new_diff的大小
                 例如交换a、b两个元素，则new_diff = sumA - a + b - (sumB - b + a) = diff - 2 * (a - b)
                 交换后应该有 |new_diff| < |diff|，否则不必进行交换
                 '''
                if abs(diff - 2 * (a[i] - b[j])) < abs(diff - new_diff):
                    new_diff = 2 * (a[i] - b[j])
                    ai, bj = i, j
        if new_diff == 0:
            break   # 交换后差绝对值不会减小，则跳出
        a[ai], b[bj] = b[bj], a[ai]  # 交换元素
        sumA = sum(a)
        sumB = sum(b)
        diff = sumA - sumB
    print(diff)
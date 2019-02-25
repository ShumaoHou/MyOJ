'''
实现Shell排序，对给定的无序数组，
按照给定的间隔变化（间隔大小即同组数字index的差），
打印排序结果，注意不一定是最终排序结果！
输入: 第一行表示测试用例个数，后面为测试用例，
每一个用例有两行，第一行为给定数组，第二行为指定间隔，每一个间隔用空格隔开。
输出: 每一行为一个用例对应的指定排序结果。
输入样例
1
49 38 65 97 76 13 27 49 55 4
5 3
输出样例
13 4 49 38 27 49 55 65 97 76
'''
def ShellInsetSort(array, len_array, dk):  # 直接插入排序
    for i in range(dk, len_array):  # 从下标为dk的数进行插入排序
        position = i
        current_val = array[position]  # 要插入的数

        index = i
        j = int(index / dk)  # index与dk的商
        index = index - j * dk

        # position>index,要插入的数的下标必须得大于第一个下标
        while position > index and current_val < array[position-dk]:
            array[position] = array[position-dk]  # 往后移动
            position = position-dk
        else:
            array[position] = current_val


def ShellSort(array, shell):  # 希尔排序
    for i in range(len(shell)):
        dk = shell[i]
        ShellInsetSort(array, len(array), dk)
    res = ""
    for i in range(len(array)):
        res += str(array[i]) + " "
    print(res.strip())

if __name__ == '__main__':
    N = int(input())
    for i in range(N):
        array = list(map(int, input().split()))
        shell = list(map(int, input().split()))
        ShellSort(array, shell)
"""
硬币最小数量
描述
Given the list of coins of distinct denominations and total amount of money.
 Output the minimum number of coins required to make up that amount.
 Output -1 if that money cannot be made up using given coins.
 You may assume that there are infinite numbers of coins of each type.
输入
The first line contains 'T' denoting the number of test cases.
Then follows description of test cases.
Each cases begins with the two space separated integers 'n' and 'amount'
denoting the total number of distinct coins and
total amount of money respectively.
The second line contains N space-separated integers A1, A2, ..., AN denoting the values of coins.
Constraints:1<=T<=30，1<=n<=100，1<=Ai<=1000，1<=amount<=100000
输出
Print the minimum number of coins required to make up that amount or return -1
if it is impossible to make that amount using given coins.
输入样例 1
2
3 11
1 2 5
2 7
2 6
输出样例 1
3
-1
"""


def min_coins(amount, coins):
    coins.sort(reverse=True)
    i = 0
    count = 0
    while True:
        if amount >= coins[i]:
            amount -= coins[i]
            count += 1
        else:
            i += 1
            if i >= len(coins):
                break
    if amount > 0:
        return -1
    else:
        return count


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, amount = map(int, input().split())
        coins = list(map(int, input().split()))
        print(min_coins(amount, coins))

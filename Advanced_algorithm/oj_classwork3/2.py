'''
素数和问题
描述
Given an even number ( greater than 2 ), return two prime numbers whose sum will be equal to given number.
There are several combinations possible. Print only first such pair.
NOTE: A solution will always exist, read Goldbach’s conjecture.
Also, solve the problem in linear time complexity, i.e., O(n).
输入
The first line contains T, the number of test cases.
The following T lines consist of a number each, for which we'll find two prime numbers.
Note: The number would always be an even number.
输出
For every test case print two prime numbers space separated, such that the smaller number appears first.
Answer for each test case must be in a new line.
输入样例
5
74
1024
66
8
9990
输出样例
3 71
3 1021
5 61
3 5
17 9973
'''
def findPrimes(N):
    for i in range(3, int(N / 2) + 1):
        if isPrime(i) and isPrime(N - i):
            return str(i) + " " + str(N - i)

# 判断N是否为质数
def isPrime(N):
    if N == 2 or N == 3:
        return True
    if N % 6 != 1 and N % 6 != 5:
        return False
    for i in range(5, int(pow(N, 0.5)) + 1):
        if N % i == 0 or N % (i + 2) == 0:
            return False
    return True

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N = int(input())
        print(findPrimes(N))
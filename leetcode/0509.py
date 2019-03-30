class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0 or N == 1:
            return N
        # return self.fib(N - 1) + self.fib(N - 2)

        f = [0] * (N + 1)
        f[0] = 0
        f[1] = 1
        for i in range(2, N + 1):
            f[i] = f[i - 2] + f[i - 1]
        return f[N]


if __name__ == '__main__':
    print(Solution().fib(10))

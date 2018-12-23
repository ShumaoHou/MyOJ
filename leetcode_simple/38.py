class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        nextRes = ""
        if n == 1:
            nextRes = "1"
            return nextRes
        res = self.countAndSay(n - 1)
        pre = res[0]
        count = 0
        for i in range(len(res)):
            now = res[i]
            if pre == now:
                count += 1
            else:
                nextRes +=  str(count) + pre
                pre = now
                count = 1
        nextRes += str(count) + pre
        return nextRes


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            n = int(line);

            ret = Solution().countAndSay(n)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
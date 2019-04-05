class RecentCounter(object):

    def __init__(self):
        self.p = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.p.append(t)
        res = 0
        for s in self.p[::-1]:
            if t - s > 3000:
                break;
            res += 1
        return res

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
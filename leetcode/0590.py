"""
给定一个 N 叉树，返回其节点值的后序遍历。
"""
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def postorder_stack(self, root):
        """
        :type root: Node
        :rtype: List[int]
        非递归-栈
        """
        if not root:
            return []
        res = []
        r = [root]
        while r:
            t = r.pop()
            if t.children:
                r.extend(t.children)
            res.append(t.val)
        res.reverse()
        return res

    def postorder_recursive(self, root):
        """
        :type root: Node
        :rtype: List[int]
        递归
        """
        res = []

        def rec(root):
            if not root:
                return res
            for c in root.children:
                rec(c)
            res.append(root.val)
            return res
        rec(root)
        return res

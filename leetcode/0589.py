"""
给定一个 N 叉树，返回其节点值的前序遍历。
"""
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def preorder_stack(self, root):
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
            res.append(t.val)
            if t.children:
                t.children.reverse()
                r.extend(t.children)
        return res

    def preorder_recursive(self, root):
        """
        :type root: Node
        :rtype: List[int]
        递归
        """
        res = []

        def rec(root):
            if not root:
                return res
            res.append(root.val)
            for c in root.children:
                rec(c)
            return res
        rec(root)
        return res

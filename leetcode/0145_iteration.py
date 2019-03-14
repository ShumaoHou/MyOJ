# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        pre = None
        if not root:
            return stack
        else:
            stack.append(root)
        while len(stack) > 0:
            t = stack[-1]
            if (t.right is None and t.left is None) or (pre is not None and (pre == t.left or pre == t.right)):
                # 两种情况需要出栈：
                # 左右子节点为空时，当前节点为叶子节点；
                # 前一节点为当前结点的子节点时，当前结点为非叶子结点；
                res.append(t.val)
                pre = t
                stack.pop()
            else:
                if t.right:
                    stack.append(t.right)
                if t.left:
                    stack.append(t.left)
        return res

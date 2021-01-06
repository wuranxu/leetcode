# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []

        def preorder(root: TreeNode):
            if root is None:
                return
            ans.append(root.val)
            preorder(root.left)
            preorder(root.right)

        preorder(root)
        return ans

    def preorderTraversalV2(self, root: TreeNode):
        """
        迭代版本遍历方式
        :param root:
        :return:
        """
        if root is None:
            return []
        ans = []
        stack = [root]
        while len(stack) > 0:
            data = stack.pop()
            if data.right is not None:
                stack.append(data.right)
            if data.left is not None:
                stack.append(data.left)
            ans.append(data.val)
        return ans

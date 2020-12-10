# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        # BFS
        if root is None:
            return []
        ans = []
        stack = [root]
        while len(stack) > 0:
            size = len(stack)
            for i in range(size):
                current = stack.pop(0)
                # 找到每一层最后一个节点的值，就是右视图那一层的值
                if i == size - 1:
                    ans.append(current.val)
                if current.left is not None:
                    stack.append(current.left)
                if current.right is not None:
                    stack.append(current.right)
        return ans

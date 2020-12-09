# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        ans = []
        while len(stack) > 0 or root is not None:
            while root is not None:
                stack.append(root)
                root = root.left
            current = stack.pop()
            ans.append(current.val)
            root = current.right
        return ans

    def inorderTraversalV2(self, root: TreeNode) -> List[int]:
        """
        递归写法
        :param root:
        :return:
        """
        ans = []

        def traversal(node: TreeNode):
            if node is None:
                return
            traversal(node.left)
            ans.append(node.val)
            traversal(node.right)

        traversal(root)
        return ans


if __name__ == "__main__":
    tree = TreeNode(1)
    tree.left = TreeNode(3)
    tree.right = TreeNode(4)
    tree.left.right = TreeNode(7)
    tree.left.left = TreeNode(5)
    s = Solution()
    print(s.inorderTraversal(tree))
    print(s.inorderTraversalV2(tree))

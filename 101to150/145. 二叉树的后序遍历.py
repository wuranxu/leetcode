# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        prev = None
        ans = []
        while len(stack) > 0 or root is not None:
            while root is not None:
                stack.append(root)
                root = root.left

            # 添加了之后开始出栈
            root = stack.pop()
            # 当当前节点存在右节点并且不等于prev的时候
            # root回栈，继续走root.right的分支
            if root.right is not None and root.right != prev:
                stack.append(root)
                root = root.right
            else:
                ans.append(root.val)
                prev = root
                # 否则这个中间节点置为None 继续走其父节点
                root = None
        return ans

    def postorderTraversalV2(self, root: TreeNode) -> List[int]:
        ans = []

        def dfs(node: TreeNode):
            if node is None:
                return None
            dfs(node.left)
            dfs(node.right)
            ans.append(node.val)

        dfs(root)
        return ans


if __name__ == "__main__":
    tree = TreeNode(1)
    tree.left = TreeNode(3)
    tree.right = TreeNode(4)
    tree.left.right = TreeNode(7)
    tree.left.left = TreeNode(5)
    s = Solution()
    print(s.postorderTraversal(tree))
    print(s.postorderTraversalV2(tree))

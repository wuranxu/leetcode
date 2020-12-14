# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        mp = {x: i for i, x in enumerate(inorder)}

        def build(preorder_left, preorder_right, inorder_left, inorder_right):
            print(preorder_left, preorder_right, inorder_left, inorder_right)
            if preorder_left > preorder_right:
                return
            root = TreeNode(preorder[preorder_left])
            i = mp[root.val]
            size = i - inorder_left
            root.left = build(preorder_left + 1, preorder_left + size, inorder_left, i)
            root.right = build(size + preorder_left + 1, preorder_right, i + 1, inorder_right)
            return root

        return build(0, len(preorder) - 1, 0, len(inorder) - 1)

        # if len(preorder) == 0:
        #     return
        # root = TreeNode(preorder[0])
        # i = 0
        # while inorder[i] != preorder[0]:
        #     i += 1
        # root.left = self.buildTree(preorder[1:i+1], inorder[:i])
        # root.right = self.buildTree(preorder[i+1:], inorder[i+1:])
        # return root


if __name__ == "__main__":
    s = Solution()
    a = [3, 9, 20, 15, 7]
    b = [9, 3, 15, 20, 7]
    s.buildTree(a, b)

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        inorder_map = {x: i for i, x in enumerate(inorder)}

        def build(inorder_left, inorder_right, postorder_left, postorder_right):
            if postorder_left > postorder_right or inorder_left > inorder_right:
                return None
            node = postorder[postorder_right]
            root = TreeNode(node)
            temp = inorder_map[node]
            size = temp - inorder_left
            root.left = build(inorder_left, temp - 1, postorder_left, postorder_left + size - 1)
            root.right = build(temp + 1, inorder_right, postorder_left + size, postorder_right - 1)
            return root

        return build(0, len(inorder) - 1, 0, len(postorder) - 1)

        # if len(postorder) == 0:
        #     return None
        # node = postorder[len(postorder) - 1]
        # root = TreeNode(node)
        # i = 0
        # while inorder[i] != node:
        #     i += 1
        # print(i)
        # root.left = self.buildTree(inorder[:i], postorder[:i])
        # root.right = self.buildTree(inorder[i+1:], postorder[i:len(postorder)-1])
        # return root


if __name__ == "__main__":
    s = Solution()
    a = [9, 3, 15, 20, 7]
    b = [9, 15, 7, 20, 3]
    result = s.buildTree(a, b)
    print(result)

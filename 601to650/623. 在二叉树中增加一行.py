# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        # 如果d是1，则直接创立一个node，并把root赋予给node.left并返回node
        if d == 1:
            node = TreeNode(v)
            node.left = root
            return node
        # 当前深度为1
        current = 1
        queue = [root]
        # 否则开始正常的bfs
        while len(queue) > 0:
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                left = node.left
                right = node.right
                # 因为要在深度的上一层进行修改，所以是d-1
                if current == d - 1:
                    node.left = TreeNode(v)
                    node.right = TreeNode(v)
                    node.left.left = left
                    node.right.right = right
                    # 添加完所有该层节点，可以直接return root了，这里用break一样
                    if i == size - 1:
                        break
                # 否则开始正常的bfs
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            current += 1
        return root

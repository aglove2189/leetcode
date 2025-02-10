# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode | None, low: int, high: int) -> int:
        stack = [root]
        total = 0
        while stack:
            node = stack.pop()
            if node.val < low:
                if node.right:
                    stack.append(node.right)
            elif node.val > high:
                if node.left:
                    stack.append(node.left)
            else:
                total += node.val
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        return total
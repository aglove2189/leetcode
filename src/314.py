from collections import defaultdict, deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def verticalOrder(root: TreeNode) -> list:
    column_table = defaultdict(list)
    queue = deque([(root, 0)])
    while queue:
        node, column = queue.popleft()
        if node:
            column_table[column].append(node.val)
            queue.append((node.left, column - 1))
            queue.append((node.right, column + 1))
    return [column_table[x] for x in sorted(column_table.keys())]

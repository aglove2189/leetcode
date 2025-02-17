class Node:
    def __init__(self, x):
        self.val = x
        self.parent = None
        self.left = None
        self.right = None


def lowestCommonAncestor(p: Node, q: Node) -> int:
    ancestors = set()
    while p:
        ancestors.add(p)
        p = p.parent
    while q:
        if q in ancestors:
            return q
        q = q.parent
    return None

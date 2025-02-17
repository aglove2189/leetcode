class NestedInteger:
    def __init__(self, value=None):
        self.value = value

    def isInteger(self):
        return isinstance(self.value, int)

    def getInteger(self):
        return self.value if self.isInteger() else None

    def getList(self):
        return self.value if not self.isInteger() else None


def depthSum(nestedList: NestedInteger) -> int:
    def dfs(nestedList, depth):
        total = 0
        for element in nestedList:
            if element.isInteger():
                total += element.getInteger() * depth
            else:
                total += dfs(element.getList(), depth + 1)
        return total
    return dfs(nestedList, 1)

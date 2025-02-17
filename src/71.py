class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        dirs = path.split("/")
        for d in dirs:
            if d == "..":
                if stack:
                    stack.pop()
            elif d and d != ".":
                stack.append(d)
        return "/" + "/".join(stack)

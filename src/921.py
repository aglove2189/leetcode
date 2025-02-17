class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        inc = 0
        for i in s:
            if i == "(":
                inc += 1
            elif i == ")":
                inc -= 1
            if inc < 0:
                count += 1
                inc = 0
        return count + inc

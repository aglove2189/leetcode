class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        result = [intervals[0]]
        for i, j in intervals[1:]:
            _, prev_j = result[-1]
            if i <= prev_j:
                result[-1][1] = max(j, prev_j)
            else:
                result.append([i, j])
        return result

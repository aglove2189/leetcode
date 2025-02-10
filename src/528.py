import random
import bisect

class Solution:
    def __init__(self, w: list[int]):
        self.prefix_sums = []
        self.total_sum = 0

        for weight in w:
            self.total_sum += weight
            self.prefix_sums.append(self.total_sum)

    def pickIndex(self) -> int:
        target = random.randint(1, self.total_sum)
        return bisect.bisect_left(self.prefix_sums, target)
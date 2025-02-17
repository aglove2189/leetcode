class SparseVector:
    def __init__(self, nums):
        self.nums = {i: val for i, val in enumerate(nums) if val != 0}

    def dotProduct(self, vec: "SparseVector") -> int:
        result = 0
        for i, val in self.nums.items():
            if i in vec.nums:
                result += val * vec.nums[i]
        return result

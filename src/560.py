class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        sum_counts = {0: 1}
        current_sum = 0
        count = 0
        for num in nums:
            current_sum += num
            count += sum_counts.get(current_sum - k, 0)
            sum_counts[current_sum] = sum_counts.get(current_sum, 0) + 1
        return count
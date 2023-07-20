class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest_sum = float('-inf')
        current_sum = 0
        for num in nums:
            current_sum += num
            if current_sum > largest_sum:
                largest_sum = current_sum
            if current_sum < 0:
                current_sum = 0
        return largest_sum
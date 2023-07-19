class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        
        indices = [idx for idx, el in enumerate(nums) if el == target]
        return [indices[0], indices[-1]]
        
        
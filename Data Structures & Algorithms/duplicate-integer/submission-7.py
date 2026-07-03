class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seen = {}
        for i, num in enumerate(nums):
            if num not in seen:
                seen[num] = i
            else:
                return True
    
        return False

            
        
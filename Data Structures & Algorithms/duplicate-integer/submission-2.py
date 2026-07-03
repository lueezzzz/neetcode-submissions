class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # nums.sort()
        # for i in range(len(nums) - 1):
        #     if nums[i] == nums[i + 1]:
        #         return True
        
        # return False
        seen = {}
        for i, num in enumerate(nums):
            if num in seen:
                return True
            else:
                seen[num] = i
        
        return False



        

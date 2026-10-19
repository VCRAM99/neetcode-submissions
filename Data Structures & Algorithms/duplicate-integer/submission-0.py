class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         y=1
         for x in nums:
            for i in nums[y:]:
                if x==i:
                    return True
            y=y+1
         return False       
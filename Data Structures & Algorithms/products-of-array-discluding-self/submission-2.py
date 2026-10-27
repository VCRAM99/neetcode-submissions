class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1]*n

        prefix = 1
        postfix = 1
        for i in range(len(nums)):
                result[i] = prefix * result[i]
                prefix = prefix * nums[i]
        for j in range(len(nums)-1,-1,-1):
                result[j] = postfix * result[j]
                postfix = postfix * nums[j]

        return result
            

        
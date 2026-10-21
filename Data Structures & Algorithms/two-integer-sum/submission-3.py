class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        difference = 0

        for i, n in enumerate(nums):
            difference = target - n
            if (difference in hashMap):
                if hashMap[difference] < i:
                    return [hashMap[difference],i]
                else:
                    return [i,hashMap[difference]]
            hashMap[n] = i
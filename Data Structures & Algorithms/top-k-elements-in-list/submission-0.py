class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequency = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = count.get(n,0) + 1
        for num,c in count.items():
            frequency[c].append(num)

        result = []
        for freq in reversed(frequency):
            for f in freq:
                result.append(f)
                if len(result)==k:
                    return result
        



        
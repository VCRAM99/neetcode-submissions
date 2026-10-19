class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        count = 1
        profit = 0
        for x in prices:
            for y in prices[count:]:
                if y-x>profit:
                    profit = y-x
            count = count+1
        return profit
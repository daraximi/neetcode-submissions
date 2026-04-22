class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxP = 0

        for r in range(1,len(prices)):
            if prices[r]< prices[l]:
                l = r
                continue
            curr = prices[r] - prices[l]
            maxP = max(curr, maxP)


        return maxP

        
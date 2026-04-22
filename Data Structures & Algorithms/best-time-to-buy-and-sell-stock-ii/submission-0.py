class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        l, r = 0, 1
        # Basically, this is a greedy problem.
        while r < len(prices):
            #profitable transaction
            if prices[r]< prices[l]:
                #buy
                l = r
            if prices[l] < prices[r]:
                #sell
                profit = prices[r] - prices[l]
                maxProfit += profit
                l = r
            r += 1
        # I want to buy all possible profits.

        return maxProfit
# 2. Best time to buy and sell stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

'''
Here, I approach two pointer solution.
it can reduce time and space complexity both.
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0,1   # define left and right pointer
        max_profit = 0  # initially define the max profit as zero

        while r<len(prices): # loop will valid when r less than the lentgh of prices list
            if prices[l] < prices[r]: # check selling price is greater than the buying price
                profit = prices[r] - prices[l]  # if greater, then it count as profit
                max_profit = max(max_profit, profit)   # find max profit to compare with prev max profit
            else:
                l = r # buying price larger, so point to the next buying price
            r += 1 # increament the selling price
        return max_profit  # return the max profit
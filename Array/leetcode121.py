from leetcode_import import *
class Solution(object):
    def maxProfit(self, prices):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        #브루트 포스 계산
        # print(prices)
        # print(prices[1:])
        # max_profit = 0
        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
        #         max_profit = max(prices[j] - prices[i],max_profit)
        #
        # return max_profit

        #
        profit = 0
        min_price = sys.maxsize
        for p in prices:
            min_price = min(min_price, p)
            profit = max(profit, p - min_price)
        return profit


s = Solution()

nums = [7,1,5,3,6,4]
print(111, s.maxProfit(nums))
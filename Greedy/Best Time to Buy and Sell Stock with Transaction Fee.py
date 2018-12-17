#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import re

class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        # start = 0
        # res = 0
        # for i in xrange(len(prices)):
        # 	if prices[i]<prices[start]:
        # 		start = i

        # 	if prices[i]-prices[start]>fee:
        # 		res += prices[i] - prices[start] - fee
        # 		start = i+1

        # return res

        cash=0
        hold=-prices[0]
        for i in range(len(prices)):
            cash=max(cash,hold+prices[i]-fee)
            hold=max(hold,cash-prices[i])

        return cash;   



if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([1,3,7,5,10,3],3))







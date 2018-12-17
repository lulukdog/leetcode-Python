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
        
        '''
        对于第i天的最大收益，应分成两种情况，一是该天结束后手里没有stock，
        可能是保持前一天的状态也可能是今天卖出了，此时令收益为cash；
        二是该天结束后手中有一个stock，可能是保持前一天的状态，也可能是今天买入了，用hold表示。
        由于第i天的情况只和i-1天有关，所以用两个变量cash和hold就可以，不需要用数组
        '''

        cash=0
        hold=-prices[0]
        for i in range(len(prices)):
            cash=max(cash,hold+prices[i]-fee)
            hold=max(hold,cash-prices[i])

        return cash;   



if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([1,3,7,5,10,3],3))







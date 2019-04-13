#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import re
import collections

class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        # dd = collections.defaultdict(lambda:0)
        # for c in S:
        #     dd[c] += 1

        # l = sorted(dd.items(), key=lambda item:item[1],reverse=True)
        
        # if l[0][1] > math.ceil(len(S)/2):
        #     return '1'
        # else:
        #     res = ''
        counter = collections.Counter(S)
        ans = "#"
        while counter:
            stop = True
            for item, times in counter.most_common():
                if ans[-1] != item:
                    ans += item
                    counter[item] -= 1
                    if not counter[item]:
                        del counter[item]
                    stop = False
                    break
            if stop: break
        return ans[1:] if len(ans) == len(S) + 1 else ""


if  __name__ == '__main__':
    s = Solution()
    print(s.reorganizeString("aabbbccccddd"))
    



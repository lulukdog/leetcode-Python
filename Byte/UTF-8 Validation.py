#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import re

class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        cnt = 0
        for d in data:
            if cnt==0:
                if d>>3 == 0b11110:
                    cnt = 3
                elif d>>4 == 0b1110:
                    cnt = 2
                elif d>>5 == 0b110:
                    cnt = 1
                elif d>>7 == 0b0:
                    cnt = 0
                else:
                    return False
            else:
                if d>>6 == 0b10:
                    cnt -= 1
                else:
                    return False

        return cnt==0



if __name__ == '__main__':
    s = Solution()
    print(s.validUtf8([235, 140, 4]))





#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import re
import heapq

def minion_game(string):
    # your code goes here
    # countStuart,countKevin = 0,0
    # vowels = ['A','E','I','O','U']
    # for i in range(len(string)):
    #     for j in range(i,len(string)):
    #         # is vowel kevin
    #         if string[i] in vowels:
    #             countKevin += 1
    #         else:
    #             countStuart+=1
    
    # if countKevin==countStuart:
    #     print 'Draw'
    # else:
    #     print 'Kevin '+str(countKevin) if countKevin>countStuart else 'Stuart '+str(countStuart)
    consonants_name,consonants_count = 'Stuart',0
    vowels_name,vowels_count = 'Kevin',0

    l = len(string)
    vowel = ['A','E','I','O','U']
    for i in range(l):
        if string[i] in vowel:
            vowels_count += l-i
        else:
            consonants_count+=l-i

    if vowels_count == consonants_count:
        print 'Draw'
    elif vowels_count > consonants_count:
        print vowels_name, vowels_count
    else:
        print consonants_name, consonants_count


if __name__ == '__main__':
    minion_game('BANANA')





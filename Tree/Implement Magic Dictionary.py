#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import re

class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = dict()
        self.chars = []
        for i in range(ord('a'),ord('z')+1):
            self.chars.append(chr(i))
        
        

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: None
        """
        for word in dict:
            for charIndex in range(0,len(word)):
                for w in self.chars:
                    if w != word[charIndex]:
                        newStr = word[0:charIndex]+w+word[charIndex+1:len(word)]
                        self.dict[newStr] = 1
        

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        if self.dict.has_key(word):
            return True
        
        return False
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)


if  __name__ == '__main__':
    o = MagicDictionary()
    o.buildDict(['hello'])
    print(o.search('hello'))
    



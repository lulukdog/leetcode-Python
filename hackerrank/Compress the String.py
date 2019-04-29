#!/bin/python

if __name__=="__main__":
    inputStr = raw_input()
    length = len(inputStr)

    denote,denoteCount,index = inputStr[0],0,0
    res = ''
    while index<length:
        if inputStr[index]==denote:
            denoteCount+=1
        else:
            res += '({:d}, {:s}) '.format(denoteCount,denote)
            denote = inputStr[index]
            denoteCount = 1
        
        index += 1

    res += '({:d}, {:s})'.format(denoteCount,denote)
    
    print res


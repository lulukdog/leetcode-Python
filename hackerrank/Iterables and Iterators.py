#!/bin/python
    
if __name__ == '__main__':
    #-------------- [self] --------------
    # length = 3
    # allStr = ['a','a','c','d']
    # number = 2

    # aIndices = []
    # for i in range(0,length+1):
    #     if allStr[i]=='a':
    #         aIndices.append(i)
    #     else:
    #         break

    # def genNextStr(nowL):
    #     nexL = nowL
    #     for i in range(len(nexL)-1,-1,-1):
    #         if nexL[i]>=length:
    #             if nexL[i-1]<length:
    #                 nexL[i-1]+=1
    #                 nexL[i] = 0
    #                 return nexL
    #             else:
    #                 nexL[i] = 0
    #                 continue
    #         else:
    #             nexL[i]+=1
    #             return nexL

    # now = [i for i in range(0,number)]
    # final = [length]*number

    # totalNum = 0
    # aNum = 0
    # while now!=final:
    #     continueTag = True
    #     for i in now:
    #         if now.count(i) > 1:
    #             continueTag = False

    #     if continueTag:
    #         for v in aIndices:
    #             if v in now:
    #                 aNum += 1
    #                 break
    #         print(now, aNum,totalNum)

    #         totalNum += 1

    #     now = genNextStr(now)

    # print float(aNum)/totalNum

    ##-------------- [by git] https://github.com/cielavenir/procon/blob/master/hackerrank/iterables-and-iterators.py
    import sys,itertools
    if sys.version_info[0]>=3: raw_input=input
    raw_input()
    a=raw_input().split()
    k=int(raw_input())
    num=0
    den=0
    for e in itertools.combinations_with_replacement(a,k):
        print e
        den+=1
        num+='a' in e
    print(num*1.0/den)


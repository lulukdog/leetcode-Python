if __name__ == '__main__':
    s = 'aabbbccde'

    from collections import defaultdict
    d = defaultdict(lambda:0)
    for char in s:
    	d[char] += 1

    def sortFuc(item1,item2):
    	if item1[1]==item2[1]:
    		return cmp(item1[0],item2[0])
    	else:
    		return -cmp(item1[1],item2[1])

    res = sorted(d.items(),cmp=lambda item1,item2:sortFuc(item1,item2))

    printCount = 0
    for i in res:
    	if printCount>=3:
    		break

    	print i[0]+' '+str(i[1])
    	printCount+=1

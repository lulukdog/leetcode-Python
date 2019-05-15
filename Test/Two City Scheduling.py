def twoCitySchedCost( costs):
    """
    :type costs: List[List[int]]
    :rtype: int
    """
    l = []
    m = {}
    for i in range(len(costs)):
        l.append(costs[i][0]-costs[i][1])
        m[i] = l[i]
    
    l1 = sorted(m.items(),key=lambda d:d[1])
    count,res = 0,0
    for i in l1:
    	print i,l1,count
        if count<len(costs)//2:
            res += costs[i[0]][0]
        else:
            res += costs[i[0]][1]

        count+=1
    
    return res


if __name__ == '__main__':
	print twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]])

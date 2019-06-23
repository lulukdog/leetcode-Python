def countTriplets(arr, r):
    setList = list(set(arr))
    setList = sorted(setList)
    if len(setList)<3:
        return 0
    
    countL = [0]*len(setList)
    index = 0
    for i in range(len(arr)):
        if arr[i]!=setList[index]:
            index += 1
        countL[index] += 1
    
    res = 0
    for i in range(2,len(countL)):
        res += countL[i-2]*countL[i-1]*countL[i]
    
    return res

if __name__ == '__main__':
	print(countTriplets([1,3,9,9,27,81],3))

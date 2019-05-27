def calHourGlassSum(x,y):
        sum = 0
        sum += arr[x][y]
        sum += arr[x][y+1]
        sum += arr[x][y+2]
        sum += arr[x+1][y+1]
        sum += arr[x+2][y]
        sum += arr[x+2][y+1]
        sum += arr[x+2][y+2]
        return sum

    res = -9*7
    for i in range(4):
        for j in range(4):
            tempRes = calHourGlassSum(i,j)
            print(tempRes)
            res = max(tempRes,res)
    
    return res

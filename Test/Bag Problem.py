# bag
def bagProblem(v,m,n):
    """
    :rtype: int
    背包问题：
    1. 状态转移公式：
    """
    row = len(v)
    res = [[0 for k in range(n)] for k in range(row)]
    for i in range(row):
        for j in range(n):
            if m[i]>j:
                res[i][j] = res[i-1][j]
            else:
                res[i][j] = max(res[i-1][j-m[i]]+v[i],res[i-1][j])

    print res
    return res[row-1][n-1]


if __name__ == '__main__':
	print bagProblem([2,12,10,7],[5,2,6,3],10)

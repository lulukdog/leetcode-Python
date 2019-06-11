class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        res = [0 for n in range(len(A)+K)]
        n = len(A)
        for i in range(n-1,-1,-1):
            ma = 0
            for j in range(i,i+K):
                if j<n:
                    ma = max(ma,A[j])
                    res[i] = max(ma*(j-i+1)+res[j+1],res[i])
        return res[0]

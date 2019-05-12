class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
            return s
        
        l = ['' for k in range(numRows)]
        t = s
        addNum,nowIndex = 1,0
        while t:
            if nowIndex==0:
                addNum=1
            elif nowIndex==numRows-1:
                addNum=-1
            
            l[nowIndex] += t[0]
            nowIndex+=addNum
            t = t[1:len(t)]
            
        strRes = ''
        for v in l:
            strRes += v
        
        return strRes
   
if __name__ == '__main__':
    s = Solution()
    s.convert("PAYPALISHIRING",3)

if __name__ == '__main__':

    def isCanStack(lCube):
        length = len(lCube)
        left,right = 0,length-1
        while left<length-1:
            if lCube[left]>=lCube[left+1]:
                left+=1
            else:
                break
        
        while right>0:
            if lCube[right-1]<=lCube[right]:
                right-=1
            else:
                break

        if left>=right-1:
            return True
        else:
            return False


    n = int(raw_input())
    for i in range(n):
        temp = raw_input()
        l = map(int,raw_input().split(' '))
        if isCanStack(l):
            print 'Yes'
        else:
            print 'No'

if __name__ == "__main__":
    lowerBegin = ord('a')
    lowerEnd = ord('z')
    upperBegin = ord('A')
    upperEnd = ord('Z')
    digitBegin = ord('0')
    digitEnd = ord('9')

    def sortFunc(v1,v2):
        o1 = ord(v1)
        o2 = ord(v2)
        if o1 in range(lowerBegin,lowerEnd+1) and o2 in range(lowerBegin,lowerEnd+1):
            return cmp(o1,o2)
        elif o1 in range(upperBegin,upperEnd+1) and o2 in range(upperBegin,upperEnd+1):
            return cmp(o1,o2)
        elif o1 in range(digitBegin,digitEnd+1) and o2 in range(digitBegin,digitEnd+1):
            if int(v1)%2==1 and int(v2)%2==0:
                return -1
            elif int(v1)%2==0 and int(v2)%2==1:
                return 1
            else:
                return cmp(o1,o2)
        else:
            return cmp(o2,o1)
    
    s = raw_input()
    res = sorted(s,cmp=lambda v1,v2:sortFunc(v1,v2))
    print(''.join(res))
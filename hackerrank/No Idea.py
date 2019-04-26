# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    l1 = map(int,raw_input().split())
    ln = map(int,raw_input().split())
    lA = map(int,raw_input().split())
    lB = map(int,raw_input().split())
    ln.sort()
    lA.sort()
    lB.sort()
    iN,iA,iB = 0,0,0
    hapiness = 0
    while iN<len(ln):
        while iA<len(lA):
            if lA[iA] == ln[iN]:
                hapiness += 1
                break
            elif lA[iA]<ln[iN]:
                iA += 1
            else:
                break

        while iB<len(lB):
            if lB[iB] == ln[iN]:
                hapiness -= 1
                break
            elif lB[iB] < ln[iN]:
                iB += 1
            else:
                break

        iN += 1
    
    print hapiness
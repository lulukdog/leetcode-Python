arr = [4,3,1,2]
begin,end = 0,len(arr)-1
swap = 0
while begin<end:
	while arr[begin]==begin+1 and begin<end:
		begin+=1
	while arr[begin]!=begin+1:
		tb,te = begin,arr[begin]-1
		arr[tb],arr[te] = arr[te],arr[tb]
		swap += 1

print(swap)

if __name__ == '__main__':
   	l=[10,20,20,10,10,30,50,10,20]

   	def cal(n,ar):
   		count,m = 0,{}
   		for i in range(n):
   			if m.has_key(ar[i]):
   				if m[ar[i]]==1:
   					count+=1
   					m[ar[i]]=0
   				else:
   					m[ar[i]]=1
   			else:
   				m[ar[i]] = 1

   		return count

   	print cal(9,l)

for i in range(int(input())):
	n,k=map(int,input().split())
	arr=list(map(int,input().split()))
	ele=[]
	for j in range(0,31):
		ele.append(0)
		for p in range(0,n):
			if arr[p]%2!=0:
				ele[j]+=1
			arr[p]=int(arr[p]/2)
	res=0

	for j in range(0,31):
		if(ele[j]%k==0):
			res+=ele[j]/k
		else:
			res+=int(ele[j]/k)+1
			
	print(int(res))
	
	
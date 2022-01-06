for _ in range(int(input())):
	n,m=map(int,input().split())
	a=list(map(int,input().split()))
	b=list(map(int,input().split()))
	mp={}
	max=10**9
	for i in range(n):
		if(i==0):
			mp[i]=0
		elif(a[i]!=0): 
			mp[i]=0
		else:
			mp[i]=max
			#print(mp)
	
	right=-1
	for i in range(n):		
		if(a[i]==1):
			right=i;
		if(right!=-1):
			if(a[i]==0):
				mp[i]=min(mp[i],i-right)
				#print(mp)
	
	left=-1
	for i in range(n-1,-1,-1):
		if(a[i]==2):
			left=i
		if(left!=-1):
				if(a[i]==0):
					mp[i]=min(mp[i],left-i)
	
					#print(mp)
	arr=[]
	for i in range(m):	
		j=b[i]-1
		if(mp[j]!=max):
			arr.append(mp[j])
		else:
			arr.append(-1)
	print(*arr)
		
			
	
	
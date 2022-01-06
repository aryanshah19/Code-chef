for i in range(int(input())):
	n=int(input())
	s=input()
	sum=0
	for i in range(n):	
		sum+=int(s[i])-0
	ans=n
	for x in range(1,n+1):
		if(n%x):
			continue
		for j in range(x):
			temp=0
			for k in range(j,n):
				if(s[k]=='1'):
					temp-=1
				else:
					temp+=1
			ans=min(ans,sum+temp)
	print(ans)
		

		
for i in range(int(input())):
	n,m=map(int,input().split())
	x,y=map(int,input().split())
	ans=[]
	for j in range(n):
		answer=input()
		F = answer.count('F')
		P = answer.count('P')
		if(F>=x or (F==x-1 and P>=y)):
			ans.append("1")
		else:
			ans.append("0")
	print(*ans, sep = "")	
	
	
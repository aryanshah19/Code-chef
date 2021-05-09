for i in range(int(input())):
	n,m=map(int,input().split())
	x,y=map(int,input().split())
	a,b=map(int,input().split())
	thief=n-x+m-y
	police=max(n-a,m-b)
	if(thief<=police):
		print("yes")
	else:
		print("no")
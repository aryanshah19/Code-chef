for i in range(int(input())):
	x,a,b=map(int,input().split())
	x=100-x
	ans=a+(x*b)
	print(ans*10)

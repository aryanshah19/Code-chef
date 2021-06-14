for _ in range(int(input())):
	D,d,p,q=map(int,input().split())
	count=0
	x=D//d
	if(x%2==0):
		count=d*((x//2)*(2*p+(x-1)*q))
	else:
		count=d*(x*(p+((x-1)//2)*q))
	count+=(D%d)*(p+x*q)
	print(int(count))
	
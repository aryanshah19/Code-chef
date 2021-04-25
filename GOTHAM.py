n=int(input())
bprint("len(p)=",len(p))
q=int(input())
for i in range(q):
	x,k=map(int,input().split())
	cost=0
	while(k!=0 and x<len(p)):
		print("x=",x)
		print("p[x-1]=",p[x-1])
		if(p[x-1]!=0):
			print("p[x-1]=",p[x-1])
			print(k)
			k=k-p[x-1]
			p[x-1]=p[x-1]-p[x-1]
			print("p[x-1]=",p[x-1])
			print(k)
			x=x+1
			cost=cost+k
			print("cost=",cost)
		else:
			x=x+1
			cost=cost+k
			print("cost=",cost)
		if(x==len(p)-1 and p[x-1]<k):
			print("in")
			cost=p[x-1]
			
	print(cost)			

for i in range(int(input())):
	N=int(input())
	boys=list(map(int,input().split()))
	girls=list(map(int,input().split()))	
	boys.sort()
	girls.sort(reverse=True)
	mix=[]
	j=0
	for a in boys:
		girls[j]=girls[j]+a
		j=j+1
	print(max(girls))
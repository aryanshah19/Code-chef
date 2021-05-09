for i in range(int(input())):
	n,hole,k=map(int,input().split())
	b=(n+1)%k
	if(hole%k==0 or hole%k==b):
		print("Yes")
	else:
		print("No")
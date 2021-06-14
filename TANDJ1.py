for _ in range(int(input())):
	a,b,c,d,k=map(int,input().split())
	ans=abs(d-b)+abs(c-a)
	print(ans)
	if(ans<=k):
		print("Yes")
	else:
		print("No")
	
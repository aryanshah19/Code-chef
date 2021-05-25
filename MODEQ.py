for i in range(int(input())):
	n,m= map(int,input().split())
	ans=0
	list = [1 for i in range(n+1)]
	for a in range(2,n+1):
		mod1=m%a
		ans=ans+list[mod1];
		print("ans=",ans,"mod1=",mod1)
		for b in range(mod1,n+1,a):
			list[b]=list[b]+1
			print(list)
			print("b=",b)
	print(ans)
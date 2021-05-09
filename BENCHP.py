
t=int(input())
for i in range(t):
	n,w,wr=map(int,input().split())
	a=list(map(int,input().split()))
	if wr>=w:
		print("YES")
	else:
		c=0
		d={}
		for i in a:
			if i in d:
				d[i]+=1
			else:
				d[i]=1
		for i in d:
			if d[i]>=2:
				t=d[i]//2
				c+=t*i*2
		if (c+wr)>=w:
			print("YES")
		else:
			print("NO")
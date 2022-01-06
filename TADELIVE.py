n,x,y=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
ab=[]
for i in range(n):
	ab.append((abs(a[i]-b[i]),i))
ab.sort()
ab.reverse()
#print(ab)
s=0
for j in range(n):
	k=ab[j][1]
	if a[k]>b[k] and x>0:
		s=s+a[k]
		x=x-1
	elif a[k]>b[k] and x==0:
		s=s+b[k]
	elif b[k]>a[k] and y>0:
		s=s+b[k]
		y=y-1
	else:
		s=s+a[k]
print(s)
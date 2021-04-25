def check(a,b):
	n=len(a)
	m=len(b)
	j=0
	i=0
	while(j < m):
		while(i < n and a[i]!=b[j]):
			i=i+1
		if(i == n):
			return True
		i=i+1
		j=j+1
	return False
def decimalToBinary(n):
	return "{0:b}".format(int(n))
t=int(input())
for i in range(t):
	s=str(input())
	ans="e"
	for j in range((1<<11)+1):
		bin=""
		if(j == 0):
			bin = "0"
		else:
			bin = decimalToBinary(j)
			print('bin=',bin)
		if(check(s, bin)):
			ans = bin
			break
		else:
			print("s=",s,"bin=",bin)
			
	print(ans)	
	
	
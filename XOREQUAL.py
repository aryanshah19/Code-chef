#for i in range(int(input())):
#	n=int(input())
#	print((2**(n-1))%1000000007) This is the answer
p=1000000007
def power(x,y,j):
	res=1
	x=x%p
	if(x==0):
		return 0
	while(y>0):
		if(y & 1):
			res=(res*x)%p
		y=int(y/2)
		x=(x*x)%p
	return res		
for i in range(int(input())):
	n=int(input())
	print(power(2,n-1,p))
		
		
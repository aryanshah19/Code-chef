def sum(num):
	sum = 0  
	while(num>0):
		sum=sum+num 
		num=num-1
	return sum	

for i in range(int(input())):
	D,N = map(int,input().split())
	for i in range(D):
		N=sum(N)
	print(N)	
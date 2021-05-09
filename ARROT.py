n=int(input())
arr=list(map(int,input().split()))
summ=sum(arr)
q=int(input())
q2=list(map(int,input().split()))
for i in range(q):
	summ*=2
	print(summ%1000000007)

	
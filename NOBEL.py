from collections import Counter

t=int(input())
for i in range(t):
	N,M=map(int,input().split())
	arr=list(map(int,input().split(' ')))
	arr.sort()
	count=len(Counter(arr).keys()) 
	if(count<M):
		print('Yes\n')
	else:
		print('No\n');


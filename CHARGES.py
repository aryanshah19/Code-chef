def printstring(s):
	count=0
	for i in range(len(s)-1):
		if(s[i+1]!=s[i]):
			count+=1
		if(s[i+1]==s[i]):
			count+=2
	print(count)
	
for _ in range(int(input())):
	n,k=map(int,input().split())
	s=list(input())
	arr=list(map(int,input().strip().split()))
	for i in arr:
		if(s[i-1]=="1"):
			s[i-1]="0"
			printstring(s)
		else:
			s[i-1]="1"
			printstring(s)

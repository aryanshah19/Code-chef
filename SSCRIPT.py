for i in range(int(input())):
	N,K=map(int,input().split(" "))
	S=input()
	flag=0
	for i in range(N):
		if(S[i]=='*'):
			flag=flag+1
		elif(S[i]!='*'):
			if(flag<K):
			 flag=0
	if(flag>=K):
		print('yes')
	else:
		print('no')
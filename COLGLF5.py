#!/usr/bin/env python3

t=int(input())   
for i in range(t):
		N,M = map(int, input().split())        
		F=list(map(int, input().split()))
		C=list(map(int, input().split()))
		mix=[]
		start=0
		f=0
		c=0
		channel=0
		s=0
		mix.extend(F)
		mix.extend(C)
		mix.sort()
		print('mix=',mix)
		for a in mix:
			print(a)
		for a in mix:
			if(a==F[0]):
				if(N-1!=f):
				 f=f+1
			elif(a==F[f] and channel==1):
				channel=0
				if(N-1!=f):
				 f=f+1
				s=s+1
			if(a==C[c] and channel==0):
				channel=1
				if(M-1!=c):
				 c=c+1
				s+=1
				
		print(s)
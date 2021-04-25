from operator import iand
from operator import ior
from functools import reduce

def displaysublist(A): 
	B = [[ ]] 
	for i in range(len(A) + 1):   
		for j in range(i + 1, len(A) + 1):         
			sub = A[i:j] 
			B.append(sub) 
	return B 

def bitwiseand(l,final):
	for k in range(1,len(l)):
		res = reduce(iand, l[k])
		final.append(res)
	return final

def printbitwiseor(a):
	res = reduce(ior, a)
	print(res)
	
for i in range(int(input())):
		n,q = map(int, input().split())        
		a=list(map(int, input().split()))
		final=[]
		bitwiseand(displaysublist(a),final)
		printbitwiseor(final)
		for i in range(q):
			x,v = map(int, input().split()) 
			a[x-1]=v
			final=[]
			bitwiseand(displaysublist(a),final)
			printbitwiseor(final)
		
	
import math
import sympy
from functools import reduce
def factors(n):    
	return set(reduce(list.__add__, 
				([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
for i in range(int(input())):
	k=int(input())
	ans=(4*k)+1
	if(sympy.isprime(ans)):
		print(6*ans)
	else:
		count=(2*k)-1
		factors_list=list(factors(ans))
		factors_list.sort()
		factors_list=factors_list[0:len(factors_list)-1]
		print(factors_list)
		for j in factors_list:
			if(j!=1):
				count1=int(((2*k)-1)/j)
				ans=ans+(count1*j)
				count=count-count1
		ans=ans+count
		print(ans)
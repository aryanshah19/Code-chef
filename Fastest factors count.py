#!/usr/bin/env python3

import math
def countDivisors(n) :
	cnt = 0
	for i in range(1, (int)(math.sqrt(n)) + 1) :
		if (n % i == 0) :
			if (n / i == i) :
				cnt = cnt + 1
				print(i)
			else : 
				cnt = cnt + 2
				
	return cnt


for _ in range(int(input())):
	n=int(input())
	print(countDivisors(n))
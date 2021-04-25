from math import gcd
for i in range(int(input())):
	N,M = map(int, input().split())     
	print(gcd(N,M),(N*M//gcd(N,M)))
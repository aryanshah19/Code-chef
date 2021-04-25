#!/usr/bin/env python3

for i in range(int(input())):
	k1,k2,k3,v=map(float,input().split(" "))
	speed1=k1*k2*k3*v
	speed=round(100/speed1,2)
	if(speed<9.58):
		print('yes')
	else:
		print('no')
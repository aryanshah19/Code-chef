import math
for i in range(int(input())):
	h,x,y,c=map(float,input().split(" "))
	if(((x+math.floor(y/2))*h)>c):
		print('No')
	else:
		print('yes')
		
	
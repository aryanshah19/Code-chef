for i in range(int(input())):
	x,y,x1,y1,d=map(int,input().split())
	food=x/x1
	water=y/y1
	if(min(food,water)>=d):
		print("yes")
	else:
		print("no")
	
	
def value(x,y):
	return int(((x*(x+1))/2)+(x*(y-1))+(((y-2)*((y-2)+1))/2))

for _ in range(int(input())):
	x1,y1,x2,y2=map(int,input().split(" "))
	answer=value(x1,y1)
	while(x1!=x2):
		x1=x1+1
		answer=answer+value(x1,y1)
	while(y1!=y2):
		y1=y1+1
		answer=answer+value(x1,y1)
	print(answer)
	
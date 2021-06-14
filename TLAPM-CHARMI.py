for _ in range(int(input())):
	x1,y1,x2,y2=map(int,input().strip().split())
	y=[1]
	for i in range(y1-1):
		y.append(y[i]+i+1)
		#print(y)  
	x=[y[-1]]
	for i in range(1,x2):
		x.append(x[i-1]+y1+i)
		#print(x)
	bottom=sum(x[x1-1:x2])
	#print(bottom)
	y_f=[1]
	for i in range(1,x2):
		y_f.append(y_f[i-1]+i+1)
		#print(y_f)  
	x_f=[y_f[-1]]   
	for i in range(1,y2):
		x_f.append(x_f[i-1]+x2-1+i)
		#print(x_f)
	right=sum(x_f[y1-1:y2])
	#print(right)
	right_f=right-x[-1]
	print(right_f+bottom)
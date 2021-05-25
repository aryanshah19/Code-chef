def y_value(x,y):
	ans=0
	for i in range(y-1):
		ans=ans+x
		x=x+1
	return ans
def value(x,y):
	return int(((x*(x+1))/2)+y_value(x,y))

def value(x,y):
	return int(((x*(x+1))/2)+(x*(y-1))+(((y-2)*((y-2)+1))/2))

print(value(10, 20))
print(value_2(10, 20))


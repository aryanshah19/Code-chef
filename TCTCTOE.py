def count_number():
	global count_o
	global count_x
	global count_space
	count_x=0
	count_o=0
	count_space=0
	row=[]
	for i in range(3):
		if(row1[i]=="O"):
			count_o=count_o+1
		if(row1[i]=="X"):
			count_x=count_x+1
		if(row2[i]=="O"):
			count_o=count_o+1
		if(row2[i]=="X"):
			count_x=count_x+1
		if(row3[i]=="O"):
			count_o=count_o+1
		if(row3[i]=="X"):
			count_x=count_x+1	
	count_space = 9 - count_x - count_o	

def check_win(symbol):
	if (row1[0] == symbol and row1[0] == row2[1] and row2[1] == row3[2]):
		return 1
	if (row1[2] == symbol and row1[2] == row2[1] and row2[1] == row3[0]):
		return 1
	for i in range(3):
		if(i==0):
			if (row1[0]==symbol and row1[0]==row1[1] and row1[1]==row1[2]):
				return 1
			if (row1[i]==symbol and row1[i] == row2[i] and row2[i] == row3[i]):
				return 1
		if(i==1):
			if (row2[0]==symbol and row2[0]==row2[1] and row2[1]==row2[2]):
				return 1
			if (row1[i]==symbol and row1[i] == row2[i] and row2[i] == row3[i]):
				return 1
		if(i==2):
			if (row3[0]==symbol and row3[0]==row3[1] and row3[1]==row3[2]):
				return 1
			if (row1[i]==symbol and row1[i] == row2[i] and row2[i] == row3[i]):
				return 1
	return 0
def check():
	global row
	row=[1,2,3]
	if (count_x < count_o):
		return 3;
	if (count_x > count_o + 1):
		return 3
	x_win = check_win('X')
	o_win = check_win('O')
	if (x_win and o_win):
		return 3
	if (x_win and count_x == count_o):
		return 3
	if (o_win and count_x > count_o):
		return 3
	if (x_win or o_win):
		return 1
	if (count_space == 0):
		return 1
	return 2
		
for i in range(int(input())):
	global row1
	global row2
	global row3
	row1=input()
	row2=input()
	row3=input()
	count_number()
	print(check())
	
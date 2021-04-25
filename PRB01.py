for k in range(int(input())):
	i=int(input())
	flag = False
	if(i==1):
		print('no')
	if i > 1:
		for j in range(2,i):
			if (i % j) == 0:
				flag = True
				break
		if flag:
			print('no')
		else:
			print('yes')
		
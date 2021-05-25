for _ in range(int(input())):
	D,d,a,b,c=map(int,input().split(" "))
	max_run=D*d
	if(max_run>=10 and max_run<21):
		print(a)
	elif(max_run>=21 and max_run<42):
		print(b)
	elif(max_run>=42):
		print(c)
	else:
		print(0)
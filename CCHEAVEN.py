for i in range(int(input())):
	l=int(input())
	s=input()
	one=0
	zero=0
	flag=0
	for j in range(l):
		if(s[j]=="0"):
			zero=zero+1
		else:
			one=one+1
		if(one>=zero):
			flag=1
			break
	if(flag==0):
		print("No")
	else:
		print("Yes")
	
def check_1(str:str):
	a=0
	for i in str:
		if(ord(i)>=97 and ord(i)<=109):
			a=a+1
		else:
			a=0
	if(a==len(str)):
		return True
	else:
		return False

def check_2(str:str):
	a=0
	for i in str:
		if(ord(i)>=78 and ord(i)<=90):
			a=a+1
		else:
			a=0
	if(a==len(str)):
		return True
	else:
		return False

for _ in range(int(input())):
	a=list(input().split(" "))
	ans=0
	for j in range(1,len(a)):
		first=False
		second=False
		if(check_1(a[j])):
			first=True
		if(check_2(a[j])):
			second=True
		if(first^ second):
			ans=ans+1
		else:
			ans=0
	if(ans==len(a)-1):
		print("YES")
	else:
		print("NO")
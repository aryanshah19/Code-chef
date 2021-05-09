for i in range(int(input())):
	n=int(input())
	ran=(2**n)-1
	count=0
	for j in range(ran):
		print(str(j)+"^("+str(j)+"+1)="+str(j^(j+1)))
		print("("+str(j)+"+2)^("+str(j)+"+3)="+str((j+2)^(j+3)),"\n")
		if(j^(j+1)==(j+2)^(j+3)):
			count=count+1
	print(count%1000000007)		
	
	
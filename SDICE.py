for i in range(int(input())):
	n=int(input())
	sum=int((n/4))*44
	rem=n%4
	if(n>=4):
		if(rem==0):
			sum=sum+16
		elif(rem==1):
			sum=sum+32
		elif(rem==2):
			sum=sum+44
		elif(rem==3):
			sum=sum+55
		print(sum)
	else:#less than 4 dices
		rem_sum=0
		if(rem==1):
			rem_sum=20
		elif(rem==2):
			rem_sum=36
		elif(rem==3):
			rem_sum=51
		print(rem_sum)
		
		
					
				



	
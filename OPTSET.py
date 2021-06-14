ans=[]
def printSubsequences(arr, index, subarr,k): 
	if index == len(arr): 
		if(len(subarr)!=0 and len(subarr)==k): 
			ans.append(subarr) 
	else: 
		printSubsequences(arr, index + 1, subarr,k) 
		printSubsequences(arr, index + 1,subarr+[arr[index]],k) 
	return ans
for i in range(int(input())):
	n,k=map(int, input().split()) 
	arr=list(range(1, n+1))
	arrays=printSubsequences(arr, 0,[],k)
	maximum=0
	index=0
	for i in range(len(arrays)):
		answer=0
		for j in range(len(arrays[i])):
			answer=answer^arrays[i][j]
		print(answer,arrays[i])
		if(answer>maximum):
			index=i
			maximum=answer
	print(*arrays[index])	
	arrays.clear()
			

	
	
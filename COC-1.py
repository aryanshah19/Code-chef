import sys
import math
def isprime(num):
    flag = True
    if (num > 1):
        for j in range(2,num):
            if (num % j) == 0:
                flag = False
                break
    return flag        
        

l = int(input())
arr=[]
prime=[]
arr=list(map(int,input().split(' ')))
for i in range(len(arr)):
    if(isprime(arr[i])):
        prime.append(arr[i])
        
if(len(prime)==0):
    print(-1)
else:
    print(max(prime))




    
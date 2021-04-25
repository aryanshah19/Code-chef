t=int(input())
for i in range(t):
    test=0
    n=int(input())
    if(n==1):
        print("no")
    else:
        for j in range(2,n):
            if n%j==0:
                print("no")
                test+=1
                break
        if (test==0):
            print("yes")
    
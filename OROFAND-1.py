for i in range(int(input())):
    n,q=map(int,input().split())
    arr=list(map(int,input().split()))
    val=[0]*31
    for i in range(n):
        for j in range(0,31):
            a= 1<<j 
            if (arr[i]&a):
                val[j]+=1 
    ans=0 
    for i in range(0,31):
        a=1<<i 
        if val[i]:
            ans+=a 
    print(ans)
    for j in range(q):
        x,v=map(int,input().split())
        for i in range(0,31):
            a=1<<i 
            if (arr[x-1]&a):
                val[i]-=1
        for i in range(0,31):
            a=1<<i 
            if (v&a):
                val[i]+=1
        arr[x-1]=v
        ans=0 
        for i in range(0,31):
            a=1<<i 
            if (val[i]>0):
                ans+=a 
        print(ans)
        
           
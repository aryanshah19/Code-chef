def CountFrequency(my_list):
    freq = {}
    for item in my_list:
            if (item in freq):
                freq[item] += 1
            else:
                freq[item] = 1
    return freq
for _ in range(int(input())):
    n,m,k=map(int,input().split())
    arr=list(map(int,input().split()))
    freq=CountFrequency(arr)
    ans=[]
    count=0
    for key,values in freq.items():
        if(key<=n and values>1):
            ans.append(key)
            count=count+1
    ans.sort()
    ans.insert(0,count)
    print(*ans)
    
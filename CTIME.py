def merge(intervals):
        intervals.sort()
        prev = intervals[0]
        res = [prev]
        for i in intervals[1:]:
            if i[1] <= prev[1]:
                continue
            elif i[0] <= prev[1]:
                i[0] = prev[0]
                res.pop()
            res.append(i)
            prev = i
        return res
for _ in range(int(input())):
    n,k,f=map(int,input().split())
    arr=[]
    total=0
    for i in range(0,n):
        l=[]
        a,b=map(int,input().split())
        l.append(a)
        l.append(b)
        arr.append(l)
    ans=merge(arr)
    for q in ans:
        total=total+q[1]-q[0]
    if(k<=f-total):
        print("yes")
    else:
        print("no")
    
    
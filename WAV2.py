from bisect import bisect_left
n,q=list(map(int,input().split()))
a=list(map(int,input().split()))
a.sort()
for i in range(q):
    x=int(input())
    pos=bisect_left(a, x)
    c=n-pos
    if pos<n and a[pos]==x:
        print(0)
    elif c%2==0:
        print("POSITIVE")
    else:
        print("NEGATIVE")
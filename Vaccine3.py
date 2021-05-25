import math
for _ in range(int(input())):
    d = 0
    a = list(map(int,input().split()))
    g,p = a[0],a[1]
    for i in range(g+2,12):
        d += a[i]
    x = d//p
    sum = a[g+1] + (d%p)
    print(x+1,end=" ")
    print(x+math.ceil(sum/p))
# cook your dish here
def findgcd(x,y):
    while y:
        x,y=y,x%y 
    return(x)
for i in range(int(input())):
    l=list(map(int,input().split()))
    l1=l[1:]
    n1=l1[0]
    n2=l1[1]
    gcd=findgcd(n1,n2)
    
    for i in range(2,len(l1)):
        gcd=findgcd(gcd,l[i])
    newlist=[]
    for i in l1:
        newlist.append(i//gcd)
    print(*newlist)
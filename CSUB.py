t = int(input())
for i in range(t):
    n = int(input())
    l = list(input())
    c = l.count('1')
    print(c*(c+1)//2)
for _ in range(int(input())):
    n=int(input())
    result=0
    for _ in range(n):
        x,y = map(int, input().split())
        result+=x-y
    print(result)

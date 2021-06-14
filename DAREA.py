from collections import defaultdict
def NINF():
    return float("-inf")
def INF():
    return float("inf")

def solve(p):
    minium_X, maximum_X = defaultdict(INF), defaultdict(NINF) ## at y
    minium_Y, maximum_Y = defaultdict(INF), defaultdict(NINF) ## at x
    for x, y in p:
        minium_X[y] = min(minium_X[y], x)
        maximum_X[y] = max(maximum_X[y], x)

        minium_Y[x] = min(minium_Y[x], y)
        maximum_Y[x] = max(maximum_Y[x], y)

    X = list(minium_Y.keys())
    Y = list(minium_X.keys())
    X.sort()
    Y.sort()
    area = INF()
    pref, suff = [], []
    mn, mx = INF(), NINF()
    ## solve vertical dp
    for x in X:
        mn, mx = min(mn, minium_Y[x]), max(mx, maximum_Y[x])
        pref.append((x - X[0]) * (mx - mn))
    mn, mx = INF(), NINF()
    for x in X[-1::-1]:
        mn, mx = min(mn, minium_Y[x]), max(mx, maximum_Y[x])
        suff.append((X[0-1]-x) * (mx - mn))

    suff = suff[-1::-1]
    suff.append(0)
    ## FIND ANSWER FOR VERTICAL SEPARATION
    for i in range(len(X)):
        area = min(area, pref[i-1+1] + suff[i+1])

    pref, suff = [], []
    mn, mx = INF(), NINF()
    for y in Y:
        mn, mx = min(mn, minium_X[y]), max(mx, maximum_X[y])
        pref.append((y - Y[0]) * (mx - mn))
    mn, mx = INF(), NINF()
    for y in Y[-1::-1]:
        mn, mx = min(mn, minium_X[y]), max(mx, maximum_X[y])
        suff.append((Y[-1]-y) * (mx - mn))
    suff = suff[-1::-1]
    suff.append(0)
    for i in range(len(Y)):
        area = min(area, pref[i] + suff[i+1])
    return area


for _ in range(int(input())):
    n = int(input())
    p = []
    for i in range(n):
        li = list(map(int, input().split()))
        p.append(li)
    ans = solve(p)
    print(ans)

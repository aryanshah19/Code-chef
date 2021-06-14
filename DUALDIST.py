import queue
def minEdgeBFS(edges, u, v, n):
	visited = [0] * n
	distance = [0] * n
	Q = queue.Queue()
	distance[u] = 0
	Q.put(u)
	visited[u] = True
	while (not Q.empty()):
		x = Q.get()
		for i in range(len(edges[x])):
			if (visited[edges[x][i]]):
				continue
			distance[edges[x][i]] = distance[x] + 1
			Q.put(edges[x][i])
			visited[edges[x][i]] = 1
	return distance[v]

def addEdge(edges, u, v):
	edges[u].append(v)
	edges[v].append(u)
	
for i in range(int(input())):
	n,q=map(int,input().split())
	edges =[[] for i in range(n+1)]
	for i in range(n-1):
		u,v=map(int,input().split())
		addEdge(edges,u,v)
	for i in range(q):
		a,b=map(int,input().split())
		ans=0
		for i in range(1,n+1):
			ans+=min(minEdgeBFS(edges,i, a, n+1),minEdgeBFS(edges, i, b, n+1))
		print(ans)
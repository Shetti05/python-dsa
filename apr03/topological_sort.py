from collections import deque

def topo_sort(V, adj):
    indegree = [0]*V
    for u in range(V):
        for v in adj[u]:
            indegree[v]+=1

    q = deque([i for i in range(V) if indegree[i]==0])
    res=[]

    while q:
        node=q.popleft()
        res.append(node)

        for nei in adj[node]:
            indegree[nei]-=1
            if indegree[nei]==0:
                q.append(nei)
    return res
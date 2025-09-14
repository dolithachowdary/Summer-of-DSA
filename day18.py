# Day 18: Important DSA Problems
# -------------------------------
# Graph Algorithms + Shortest Paths + MST
# These are very important for interviews and competitive programming.
# -------------------------------

from collections import deque
import heapq

# -------------------------------------------------------------------
# 1. Detect Cycle in Undirected Graph (using BFS)
# Idea:
#   - In BFS, we keep track of (node, parent).
#   - If we encounter a visited neighbor which is NOT parent → cycle exists.
# -------------------------------------------------------------------

def is_cycle_bfs(v, adj):
    visited = [0] * v   # keep track of visited nodes
    
    for start in range(v):  # check all components
        if not visited[start]:
            q = deque([(start, -1)])   # (node, parent)
            visited[start] = 1
            
            while q:
                node, parent = q.popleft()
                for neigh in adj[node]:
                    if not visited[neigh]:
                        visited[neigh] = 1
                        q.append((neigh, node))
                    elif neigh != parent:  # visited neighbor but not parent
                        return True
    return False

print("Cycle (BFS):", is_cycle_bfs(5, [[1], [0,2], [1,3,4], [2,4], [2,3]]))  # True


# -------------------------------------------------------------------
# 2. Topological Sort (Kahn’s Algorithm - BFS)
# Works only on Directed Acyclic Graph (DAG).
# Idea:
#   - Compute indegree of each node.
#   - Push nodes with indegree=0 into queue.
#   - Repeatedly remove nodes and decrease indegree of neighbors.
#   - Result is a valid topological order.
# -------------------------------------------------------------------

def topo_sort(v, adj):
    indegree = [0]*v
    for u in range(v):
        for neigh in adj[u]:
            indegree[neigh]+=1
    
    q = deque([i for i in range(v) if indegree[i]==0])  # start with 0 indegree nodes
    topo = []
    
    while q:
        node = q.popleft()
        topo.append(node)
        for neigh in adj[node]:
            indegree[neigh]-=1
            if indegree[neigh]==0:
                q.append(neigh)
    
    return topo

print("Topo Sort:", topo_sort(6, [[2,3],[3,4],[5],[5],[],[]]))  # Example DAG


# -------------------------------------------------------------------
# 3. Dijkstra’s Algorithm (Shortest Path in Weighted Graph)
# Works for graphs with NON-NEGATIVE weights.
# Idea:
#   - Use priority queue (min-heap) to greedily pick smallest distance node.
#   - Relax edges of that node.
#   - Continue until all shortest distances are found.
# Time Complexity: O((V+E) log V)
# -------------------------------------------------------------------

def dijkstra(v, adj, src):
    dist = [float('inf')] * v
    dist[src] = 0
    pq = [(0, src)]   # (distance, node)
    
    while pq:
        d, node = heapq.heappop(pq)
        if d > dist[node]:
            continue
        for neigh, wt in adj[node]:
            if dist[node] + wt < dist[neigh]:
                dist[neigh] = dist[node] + wt
                heapq.heappush(pq, (dist[neigh], neigh))
    return dist

# Graph: adj[u] = [(v, weight), ...]
print("Dijkstra:", dijkstra(5, [[(1,2),(2,4)], [(2,1),(3,7)], [(4,3)], [(4,1)], []], 0))


# -------------------------------------------------------------------
# 4. Bellman-Ford Algorithm (Detect Negative Cycles + Shortest Paths)
# Works with NEGATIVE weights.
# Idea:
#   - Relax all edges (V-1) times.
#   - If we can relax again in V-th iteration → Negative Cycle exists.
# Time Complexity: O(V*E)
# -------------------------------------------------------------------

def bellman_ford(v, edges, src):
    dist = [float('inf')] * v
    dist[src] = 0
    
    # Relax edges v-1 times
    for _ in range(v-1):
        for u, v_, wt in edges:
            if dist[u] != float('inf') and dist[u]+wt < dist[v_]:
                dist[v_] = dist[u]+wt
    
    # Check for negative cycle
    for u, v_, wt in edges:
        if dist[u] != float('inf') and dist[u]+wt < dist[v_]:
            return "Negative Cycle Detected"
    
    return dist

edges = [(0,1,2),(1,2,-1),(2,3,2),(3,1,-2)]
print("Bellman-Ford:", bellman_ford(4, edges, 0))


# -------------------------------------------------------------------
# 5. Disjoint Set Union (Union-Find) + Kruskal’s MST
# DSU (Union-Find):
#   - Helps check if two nodes belong to same component.
#   - Union by rank + Path compression optimizes performance.
#
# Kruskal’s Algorithm:
#   - Sort all edges by weight.
#   - Pick the smallest edge that does not form a cycle (using DSU).
#   - Continue until MST is formed.
# -------------------------------------------------------------------

class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]  # each node is its own parent
        self.rank = [0]*n
    
    def find(self, x):
        # Path compression: attach node directly to root
        if self.parent[x]!=x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr==yr: return False  # already connected
        # Union by rank
        if self.rank[xr]<self.rank[yr]:
            self.parent[xr]=yr
        elif self.rank[xr]>self.rank[yr]:
            self.parent[yr]=xr
        else:
            self.parent[yr]=xr
            self.rank[xr]+=1
        return True

def kruskal(n, edges):
    dsu = DSU(n)
    mst = 0
    edges.sort(key=lambda x:x[2])  # sort by weight
    for u,v,w in edges:
        if dsu.union(u,v):
            mst+=w  # include edge in MST
    return mst

edges = [(0,1,10),(0,2,6),(0,3,5),(1,3,15),(2,3,4)]
print("Kruskal MST:", kruskal(4, edges))

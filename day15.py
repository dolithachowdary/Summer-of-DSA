# -----------------------------
# 📘 Day 15: Graphs
# -----------------------------
# Covers:
# 1. Adjacency List Construction
# 2. BFS Traversal
# 3. DFS Traversal
# 4. Number of Islands (Grid DFS)
# 5. Flood Fill (Grid DFS)
# 6. Connected Components in Graph
# 7. Cycle Detection in Undirected Graph
# 8. Cycle Detection in Directed Graph (DFS)
# 9. Topological Sort (DFS + BFS Kahn’s Algorithm)
# -----------------------------

# ------------------------------------
# Create Adjacency List of a Graph
# Inputs: v (vertices), e (edges), edge list
# Output: adjacency list
# ------------------------------------
def adjlist(v, e, edge):
    adj = [[] for _ in range(v)]  # create v empty lists
    for n, m in edge:             # for every edge (u,v)
        adj[n].append(m)
        adj[m].append(n)          # undirected graph
    return adj


# ------------------------------------
# BFS Traversal in Graph
# ------------------------------------
def bfs(adj):
    v = len(adj)
    visit = [0] * v
    ans = []
    q = []
    start = 0  # start BFS from node 0
    if visit[start] == 0:
        visit[start] = 1
        q = [start]
        while q:
            node = q.pop(0)
            ans.append(node)
            for i in adj[node]:
                if visit[i] == 0:
                    visit[i] = 1
                    q.append(i)
    return ans


# ------------------------------------
# DFS Traversal in Graph
# ------------------------------------
def depth(node, visited, adj, ans):
    visited[node] = 1
    ans.append(node)
    for i in adj[node]:
        if visited[i] == 0:
            depth(i, visited, adj, ans)

def dfs(adj):
    v = len(adj)
    visited = [0] * v
    ans = []
    node = 0
    if visited[node] == 0:
        depth(node, visited, adj, ans)
    return ans


# ------------------------------------
# Number of Islands in a Grid
# ------------------------------------
def recur(i, j, grid, visited, n, m):
    visited[i][j] = 1
    for row, col in [[-1,0],[1,0],[0,-1],[0,1]]:
        delrow, delcol = i+row, j+col
        if (0 <= delrow < n and 0 <= delcol < m 
            and grid[delrow][delcol] == '1' 
            and visited[delrow][delcol] == 0):
            recur(delrow, delcol, grid, visited, n, m)

def no_of_islands(grid):
    n, m = len(grid), len(grid[0])
    visited = [[0]*m for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '1' and visited[i][j] == 0:
                recur(i, j, grid, visited, n, m)
                count += 1
    return count


# ------------------------------------
# Flood Fill (DFS version)
# ------------------------------------
def recur_fill(i, j, image, n, m, color, original):
    image[i][j] = color
    for row, col in [[-1,0],[1,0],[0,-1],[0,1]]:
        delrow, delcol = i+row, j+col
        if (0 <= delrow < n and 0 <= delcol < m 
            and image[delrow][delcol] == original):
            recur_fill(delrow, delcol, image, n, m, color, original)

def floodfill(image, sr, sc, color):
    n, m = len(image), len(image[0])
    original = image[sr][sc]
    if image[sr][sc] != color:
        recur_fill(sr, sc, image, n, m, color, original)
    return image


# ------------------------------------
# Connected Components in Graph
# ------------------------------------
def connected_components(adj):
    v = len(adj)
    visited = [0]*v
    components = []
    for i in range(v):
        if visited[i] == 0:
            ans = []
            depth(i, visited, adj, ans)
            components.append(ans)
    return components


# ------------------------------------
# Cycle Detection in Undirected Graph
# ------------------------------------
def is_cycle_undirected(adj):
    v = len(adj)
    visited = [0]*v
    from collections import deque
    
    for start in range(v):
        if not visited[start]:
            q = deque([(start, -1)])
            visited[start] = 1
            while q:
                node, parent = q.popleft()
                for nei in adj[node]:
                    if not visited[nei]:
                        visited[nei] = 1
                        q.append((nei, node))
                    elif parent != nei:  # back-edge found
                        return True
    return False


# ------------------------------------
# Cycle Detection in Directed Graph (DFS)
# ------------------------------------
def is_cycle_directed(v, adj):
    visited = [0]*v
    path = [0]*v
    
    def dfs_cycle(node):
        visited[node] = 1
        path[node] = 1
        for nei in adj[node]:
            if not visited[nei]:
                if dfs_cycle(nei): return True
            elif path[nei]:  # back-edge found
                return True
        path[node] = 0
        return False
    
    for i in range(v):
        if not visited[i]:
            if dfs_cycle(i): return True
    return False


# ------------------------------------
# Topological Sort using DFS
# ------------------------------------
def topo_sort_dfs(v, adj):
    visited = [0]*v
    stack = []
    def dfs_topo(node):
        visited[node] = 1
        for nei in adj[node]:
            if not visited[nei]:
                dfs_topo(nei)
        stack.append(node)
    for i in range(v):
        if not visited[i]:
            dfs_topo(i)
    return stack[::-1]


# ------------------------------------
# Topological Sort using BFS (Kahn’s Algorithm)
# ------------------------------------
def topo_sort_bfs(v, adj):
    indeg = [0]*v
    for u in range(v):
        for vtx in adj[u]:
            indeg[vtx] += 1
    from collections import deque
    q = deque([i for i in range(v) if indeg[i] == 0])
    topo = []
    while q:
        node = q.popleft()
        topo.append(node)
        for nei in adj[node]:
            indeg[nei] -= 1
            if indeg[nei] == 0:
                q.append(nei)
    return topo


# -----------------------------
# ✅ Sample Test Runs
# -----------------------------
print("BFS:", bfs([[2, 3, 1], [0], [0, 4], [0], [2]]))
print("DFS:", dfs([[2, 3, 1], [0], [0, 4], [0], [2]]))

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print("No. of Islands:", no_of_islands(grid))
print("Flood Fill:", floodfill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))

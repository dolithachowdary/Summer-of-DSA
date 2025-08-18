# graphs:

# return adj list of the graph inputs: v,e,edges

def adjlist(v,e,edge):
    adj=[]
    for i in range (v):
        adj.append([])
    for n,m in edge:
        adj[n].append(m)
        adj[m].append(n)  #undirected
    return adj

# bfs traversal in graph :

def bfs(adj):
    v=len(adj)
    visit=[0]*v
    start=0
    ans=[]
    q=[]
    if (visit[start]==0):
        visit[start]=1
        q=[start]
        while(q):
            node=q.pop(0)
            ans.append(node)
            for i in adj[node]:
                if(visit[i]==0):
                    visit[i]=1
                    q.append(i)
        return ans
print(bfs([[2, 3, 1], [0], [0, 4], [0], [2]]))

# dfs traversal in graph:

def depth(node,visited,adj,ans):
    visited[node]=1
    ans.append(node)
    for i in adj[node]:
        if (visited[i]==0):
            depth(i,visited,adj,ans)
#Function to return a list containing the DFS traversal of the graph.
def dfs(adj):
    
    v=len(adj)
    visited=[0]*v
    ans=[]
    node=0
    if visited[node]==0:
        depth(node,visited,adj,ans)
    return ans
print(dfs([[2, 3, 1], [0], [0, 4], [0], [2]]))

# no of islands:
def recur(i,j,grid,visited,n,m):
    visited[i][j]=1
    for row,col in [[-1,0],[1,0],[0,-1],[0,1]]:
        delrow=i+row
        delcol=j+col
        if(delrow>=0 and delrow<n and delcol>=0 and delcol<m and grid[delrow][delcol]=='1' and visited[delrow][delcol]==0):
            recur(delrow,delcol,grid,visited,n,m)


def no_of_islands(grid):
    n=len(grid)
    m=len(grid[0])
    visited=[]
    for i in range(n):
        temp=[0]*m
        visited.append(temp)
    count=0
    for i in range(n):
        for j in range(m):
            if(grid[i][j]=='1' and visited[i][j]==0):
                recur(i,j,grid,visited,n,m)
                count+=1
    return count

print(no_of_islands( [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))
            
# flood fill:

def recur(i,j,image,n,m,color,original):
    image[i][j]=color
    for row,col in [[-1,0],[1,0],[0,-1],[0,1]]:
        delrow=i+row
        delcol=j+col
        if(delrow>=0 and delrow<n and delcol>=0 and delcol<m and image[delrow][delcol]==original):
            recur(delrow,delcol,image,n,m,color,original)

def floodfill(image,sr,sc ,color):
    n=len(image)
    m=len(image[0])
    original=image[sr][sc]

    if(image[sr][sc]!=color):
        recur(sr,sc,image,n,m,color,original)
    return image

print(floodfill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))

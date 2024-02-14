def dfs(g, i, visited):
    visited[i] = 1
    print(chr(ord('A')+i), end=' ')
    for j in range(len(g)):
        if g[i][j] == True and not visited[j]:
            dfs(g,j,visited)

graph = [
    [0,0,1,1,0],
    [0,0,1,0,0],
    [1,1,0,1,1],
    [1,0,1,0,0],
    [0,0,1,0,0]
]
visited = [False] * len(graph)
if __name__ == "__main__":
    dfs(graph,0,visited)
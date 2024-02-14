# 재귀 함수로 구현함.
# preorder traversal
# inorder traversal
# postorder traversal

# 깊이 우선 탐색
def dfs(g, v, visited):
    visited[v] = 1
    print(chr(ord('A')+v), end=' ')
    for i in range(len(g)):
        if g[v][i] == True and not visited[i]:
            dfs(g,i,visited)

graph = [
    [0,1,0,1,0],
    [1,0,1,1,0],
    [0,1,0,0,1],
    [1,1,0,0,1],
    [0,0,1,1,0]
]
visited = [False] * len(graph)

if __name__ == "__main__":
    dfs(graph,0,visited)
#DFS메서드 정의
def dfs(graph, v, visited):
    #v는 시작 노드
    visited[v]=True
    print(v, end = ' ')
    for i in graph[v]:
        if not visited[i]:#방문 안했으면
            dfs(graph, i, visited)

#각자 노드와 어떤 노드가 연결되어있는지
graph=[
    [], #0번 노드는 없는것으로..
    [2,3,8],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited=[False] * 9
dfs(graph, 1, visited)#스택에 들어간 순서 출력

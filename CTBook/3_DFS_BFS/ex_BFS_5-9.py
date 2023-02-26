from collections import deque

#BFS메서드 정의
def bfs(graph, start, visited):
    queue=deque([start])
    visited[start]=True

    while queue: #큐가 빌때까지 반복 /queue=0이 되면 탈출
        v=queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not visited[i]: #방문 안했으면
                queue.append(i)
                visited[i]=True

graph=[
    [],  # 0번 노드는 없는것으로..
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited=[False]*9
bfs(graph,  1, visited)
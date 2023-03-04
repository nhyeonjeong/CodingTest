'''
시작시점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색가늫아기 때문에 BFS가 적절
'''

from collections import deque

height, width = map(int, input().split())
graph=[]
for i in range(height):
    graph.append(list(map(int,input())))

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def bfs(x,y):
    queue=deque()
    queue.append([x,y])
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            #벽이거나 범위를 넘어서면 continue
            if nx<0 or ny<0 or nx>=height or ny>=width:
                continue
            if graph[nx][ny]==0:
                continue

            if graph[nx][ny]==1:#방문한 경우
                graph[nx][ny]=graph[x][y]+1
                queue.append([nx,ny])
            #else: 2-4.py에서는 방문하지 않은경우도 해줬지만 안해줘도 된다(이미 방문한게 더 최단거리가 써져있을테니까)
    return graph[height-1][width-1]

print(bfs(0,0))

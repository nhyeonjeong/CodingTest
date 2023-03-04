from collections import deque

height, width=map(int,input().split())
graph=[]
for i in range(height):
    graph.append(list(map(int,input())))

#dfs로 풀것임-->bfs로 변경
# def dfs(x,y):
#     global cnt
#     if x<1 or x>height or y<1 or y>width:
#         return
#     if x==height and y==width:
#         cnt.append()
#     dfs(x-1, y)
#     dfs(x,y+1)
#     dfs(x+1, y)
#     dfs(x,y-1)
#
#
# cnt=[]
# print(min(cnt))
dx=[-1,0,1,0]
dy=[0,1,0,-1]
nx,ny=0,0
def bfs(graph,x,y):

    queue=deque([[x,y]])
    # graph[x][y]=1
    while queue:

        xy=queue.popleft()
        for i in range(4):
            nx=xy[0]+dx[i]
            ny=xy[1]+dy[i]
            if nx<0 or nx>= height or ny<0 or ny>=width or graph[nx][ny]==0:
                continue

            if graph[nx][ny]!=1: #이동했는데 2이상의 숫자이면(이미 방문했던것)
                new=min(graph[xy[0]][xy[1]]+1, graph[nx][ny])
                graph[nx][ny]=new

            else: #이동했는데 1이면 그냥 갱신만 해주기
                graph[nx][ny]=graph[xy[0]][xy[1]]+1
                queue.append([nx,ny])

bfs(graph,0,0)
print(graph[height-1][width-1])

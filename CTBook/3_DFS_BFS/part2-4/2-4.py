from collections import deque

height, width=map(int,input().split())
graph=[]
for i in range(height+1):
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
def bfs(x,y):
    if x < 1 or x > height or y < 1 or y > width:
        return


print(graph[height][width])
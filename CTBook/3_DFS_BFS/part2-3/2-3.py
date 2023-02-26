#BFS를 사용한 문제풀이
from collections import deque

height, width=map(int,input().split())
box=[]

#얼음틀 입력받기
for i in range(height):
    box.append(list(map(int,input())))

#동서남북 탐방을 위함
dx=[-1,0,1,0]
dy=[0,1,0,-1]
nx,ny=0,0

#결과
icecream=0
def bfs(box, j, k):
    global icecream

    #visited = []  # 방문할때마다 append로 넣기->필요없는 것 같아서 뺀다.어차피 방목할때 0에서 1로 바꿔줄테니까

    icecream+=1 #아이스크림 수 +1
    box[j][k]=1 #얼음틀 갱신

    #큐 생성(BFS)
    queue=deque([[j,k]]) #처음 큐 만들때 주의 -->[[j,k]]로 해야 배열로 들어감
    #visited.append([j,k])
    while queue: #큐가 빌때까지 반복
        xy=queue.popleft() #큐에서 pop
        for i in range(4): #동서남북 탐색
            nx=xy[0]+dx[i]
            ny=xy[1]+dy[i]

            #범위벗어나거나 이미 방문했거나 막혀있으면 다시 for문 처음으로
            if nx < 0 or nx >= height or ny < 0 or ny >= width or box[nx][ny]==1:
                continue

            # 방문안했던 거라면
            # if [nx,ny] not in visited:
            #     box[nx][ny]=1
            #     visited.append([nx,ny])
            #     queue.append([nx,ny])

            box[nx][ny]=1
            queue.append([nx,ny])

for j in range(height):
    for k in range(width):
        if box[j][k]==0:
            bfs(box, j, k) #너비우선탐색 함수

print(icecream)
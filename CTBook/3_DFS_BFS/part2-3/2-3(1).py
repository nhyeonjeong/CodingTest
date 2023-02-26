#문제집-DFS를 사용한 문제풀이
height, width=map(int,input().split())
box=[]

#얼음틀 입력받기
for i in range(height):
    box.append(list(map(int,input())))

def dfs(x,y):
    #범위 벗어나면
    if x<=-1 or x>=height or y<=-1 or y>=width:
        return False
    #현재 노드 아직 방문하지 않았으면
    if box[x][y]==0:
        box[x][y]=1
        dfs(x-1, y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    #현재노드 방문했으면 False를 반환
    return False

result=0
for i in range(height):
    for j in range(width):
        if dfs(i,j)==True:
            result+=1

print(result)
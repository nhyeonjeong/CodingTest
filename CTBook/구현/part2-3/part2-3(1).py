height, width=map(int, input().split())

#방문 위치 저장용 d
d=[[0]*width for _ in range(height)]

row, column, direction=map(int,input().split())
d[row][column]=1#현재를 방문처리

#
array=[]
for i in range(height):
    array.append(list(map(int,input().split())))

drow=[-1, 0, 1, 0]
dcolumn=[0, 1, 0, -1]

def turn_left():
    global direction, rotate
    direction-=1
    if direction==-1:
        direction=3
    rotate+=1

#결과변수
cnt=1
rotate=0
nrow, ncolumn=0, 0
while True:
    turn_left()#왼쪽으로 회전(for문을 사용하지 않았음)
    nrow=row+drow[direction]
    ncolumn=column+dcolumn[direction]
    if d[nrow][ncolumn]==0 and array[nrow][ncolumn]==0: #and여야 방문하지 않은것
        d[nrow][ncolumn]=1#방문처리
        row=nrow
        column=ncolumn
        cnt+=1
        rotate=0 #이동하면 다시 0으로 리셋
        continue
    # else:
    #     rotate+=1

    if rotate==4:
        #뒤로 빼보기
        nrow=row-drow[direction]
        ncolumn=column-dcolumn[direction]
        if array[nrow][ncolumn]==0: #바다가 아니라면 방문했든 안했든 뒤로간다
            row=nrow
            column=ncolumn
        else:
            break
        rotate=0#뒤로가면 다시 리셋
print(cnt)




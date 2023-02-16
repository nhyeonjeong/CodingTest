'''
오류 존재 코드!!!!
:회전시 보고있는 방향에서 왼쪽먼저 살펴야되는데
처음에 보고있는 데부터 확인함..

-->오류 수정완료
'''

height,width=map(int, input().split())
row,column,direction=map(int, input().split())
#box입력받기
box=[]
for h in range(height):
    box.append(list(map(int, input().split())))

box[row][column]=2#현재를 방문처리#주의

#간 곳을 2로 바꾸자
nesw=[[-1,0],[0,1],[1,0],[0,-1]]#동쪽은 east
next_r,next_c=0,0 #다음에 갈 곳 r,c계산 위한 변수
cnt=1 #방문한 칸의 수
while True:
    #왼쪽방향 회전
    rotate=0
    for i in range(4):
        #왼쪽으로 회전 먼저
        direction-=1
        if direction==-1:
            direction=3
        next_r=row+nesw[direction][0]
        next_c=column+nesw[direction][1]
        if box[next_r][next_c]==0: #가본적없으면
            cnt+=1#방문
            row=next_r
            column=next_c
            box[row][column]=2
            break

        rotate+=1

    #주변이 모두 바다이거나 방문해봤다면 cnt=4일것->뒤로 한 칸 가기
    if rotate==4:
        next_r=row+nesw[direction-2][0]
        next_c=column+nesw[direction-2][1]
        if box[next_r][next_c]==1:
            break #탐색 끝
        else:
            #한 칸 뒤로 가기
            row=next_r
            column=next_c

print(cnt)


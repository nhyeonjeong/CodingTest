start=input()
#입력받고 미리 문자를 숫자로 바꿔주기
column=ord(start[0])-ord('a')+1
row=int(start[1])

direction=[[1,2],[-1,2],[2,-1],[2,1],[1,-2],[-1,-2],[-2,1],[-2,-1]]
cnt=0
for step in direction:
    next_row=row+step[0]
    next_column=column+step[1]
    if next_row>=1 and next_row<=8 and next_column>=1 and next_column<=8:
        cnt+=1
print(cnt)
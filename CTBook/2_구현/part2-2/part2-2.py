start=input()
direction=[[1,2],[-1,2],[2,-1],[2,1],[1,-2],[-1,-2],[-2,1],[-2,-1]]
nextr, nextc=0,0
cnt=0
for i in range(len(direction)):
    nextr=ord(start[0])+direction[i][0]
    nextc=int(start[1])+direction[i][1]
    if nextr<ord('a') or nextr>ord('h') or nextc<1 or nextc>8 :
        continue
    else:
        cnt+=1
print(cnt)
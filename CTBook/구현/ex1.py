boxscale=int(input())
direction=list(input().split())
direction2=['R','L','U','D']
direction3=[[0,1],[0,-1],[-1,-0],[1,0]]
left,right=1,1
nextleft,nextright=0,0
box=[[0 for _ in range(boxscale+1)]for _ in range(boxscale+1)]
for i in range(len(direction)):
    for j in range(len(direction2)):
        if direction[i]==direction2[j]:
            nextleft=left+direction3[j][0]
            nextright=right+direction3[j][1]
            if 1>nextleft or nextleft>boxscale or nextright<1 or nextright>boxscale:
                break
            else: #범위안에 잘 들어와있다
                left=nextleft
                right=nextright
                break
print(left,right)

n,m,k=map(int, input().split())
numbers=list(map(int, input().split())) #배열입력받기
numbers.sort()
bb=numbers[-1] #배열에서 제일 큰 수
b=numbers[-2] #배열에서 그 다음으로 큰 수

l,sum_num=0,0
while True:
    for _ in range(k):
        if l==m:
            break
        sum_num+=bb
        l+=1 #더해준 횟수를 세기 위해
    #break을 제일 밑에 써주면 안됨
    if l == m:
        break
    sum_num+=b
    l+=1
    # if l==m:
    #     break

print(sum_num)
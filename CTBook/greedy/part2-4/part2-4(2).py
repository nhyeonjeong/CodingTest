#n의 범위가 클수록 제일 최적의 코드임(n-=1을 일일이 안해줘도 되니까)
n,k=map(int, input().split())
count=0

while True :
    target=(n//k)*k
    count+=(n-target)
    n=target

    if n<k:
        break
    n//=k
    count+=1

count+=(n-1) #마지막에 0이 아닌 1이 될때까지니까
print(count)

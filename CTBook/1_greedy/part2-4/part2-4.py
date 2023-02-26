n,k=map(int, input().split())
count=0

while n!=1:
    while n%k!=0:
        n-=1
        count+=1
        if n==1:
            break
    while n%k==0:
        n/=k
        count+=1

print(count)
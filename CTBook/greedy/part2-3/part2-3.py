n,m=map(int,input().split())
max=0
for i in range(n):
    numbers=list(map(int, input().split()))
    numbers.sort()
    if max<numbers[0]:
        max=numbers[0]
print(max)
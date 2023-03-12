n,change=map(int,input().split())

array_a=list(map(int,input().split()))
array_b=list(map(int,input().split()))

array_a.sort()
array_b.sort()

for i in range(change):
    if array_a[i]<array_b[n-1-i]:
        array_a[i],array_b[n-1-i]=array_b[n-1-i],array_a[i]
print(sum(array_a))

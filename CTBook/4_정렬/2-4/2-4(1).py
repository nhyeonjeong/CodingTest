n,change=map(int,input().split())

array_a=list(map(int,input().split()))
array_b=list(map(int,input().split()))

array_a.sort()
array_b.sort(reveerse=True)

for i in range(change):
    if array_a[i]<array_b[i]:
        array_a[i],array_b[i]=array_b[i],array_a[i]
    else:
        break #array_a[i]가 같거나 더 커지는 순간 교체하는게 의미없어짐
print(sum(array_a))

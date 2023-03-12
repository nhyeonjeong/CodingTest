#정렬라이브러리 sorted() key 활용
n=int(input())
array=[]
for i in range(n):
    array.append(list(input().split()))

def setting(data):
    return data[1]
array=sorted(array, key=setting)
for namescore in array:
    print(namescore[0],end=' ')
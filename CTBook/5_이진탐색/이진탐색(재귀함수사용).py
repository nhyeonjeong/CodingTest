def binary_search(array, target,start,end):
    if start>end:#target이 array에 없으면 발생
        return None
    mid=(start+end)//2

    if array[mid]==target:
        return mid
    elif array[mid]>target:
        return binary_search(array,target,start,mid-1)
    else:
        return binary_search(array,target,mid+1,end) #여기서 함수 호출하고 다음은 실행하면 안되니까 return하는거

n,target=list(map(int,input().split()))
array=list(map(int,input().split()))

result=binary_search(array,target, 0,n-1)
if result==None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1)


#퀵정렬은 재귀함수 필요

array=[7,5,9,0,3,1,6,2,4,8]
#array=[9,6,1]
def quick_sort(array,start, end):
    if start>=end:#숫자 한개 남거나 엇갈리면 탈출
        return
    pivot=start
    left=start+1
    right=end
    while left<=right:
        #피벗보다 큰 데이터 찾을떄까지
        while left<=end and array[left]<=array[pivot]: #left<=end부터 만족하지 않으면 and이후의 조건은 실행도 안해보는듯??
            left+=1
        #피벗보다 작은 데이터 찾을때까지
        while right>start and array[right]>=array[pivot]: #밑에서 right과 pivot을 바꿀수도 있기 떄문에 right은 array인덱스 범위를 벗어나면 안됨-->따라서 right>=start불가
            right-=1

        if left>right:#엇갈리면
            array[right],array[pivot]=array[pivot],array[right]
        else:
            array[left],array[right]=array[right],array[left]

    quick_sort(array,start, right-1)#right과 pivot이 교차하고 끝났으니까
    quick_sort(array,right+1, end)

quick_sort(array,0,len(array)-1)
print(array)


#2_파이썬 장점을 살린 퀵정렬
def quick_sort2(array):
    if len(array)<=1:
        return array

    pivot=array[0]
    tail=array[1:]

    left_side=[x for x in tail if x<=pivot]
    right_side=[x for x in tail if x>pivot]

    return quick_sort2(left_side) + [pivot] + quick_sort2(right_side)

print(quick_sort2(array))
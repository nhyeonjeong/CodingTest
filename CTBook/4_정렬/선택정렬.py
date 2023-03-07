array=[7,5,9,0,3,1,6,2,4,8]
for i in range(len(array)-1): #맨마지막거는 알아서 제일 큰 수가 됨->n-1번만 반복하면 됨
    min_index=i
    for j in range(i+1, len(array)):
        if array[min_index]>array[j]:
            min_index=j
    array[i],array[min_index]=array[min_index],array[i]

print(array)
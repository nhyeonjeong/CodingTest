n = int(input())
array1 = list(map(int, input().split()))

m = int(input())
array2 = list(map(int, input().split()))

array1.sort()

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array1[mid] == t:
            return "yes"

        elif array1[mid] > t:
            end = mid - 1
        else:
            start = mid + 1

    return "no"

for t in array2:
    print(binary_search(array1,t,0,n-1),end=' ')


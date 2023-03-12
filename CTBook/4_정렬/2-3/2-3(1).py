n=int(input())
array=[]
for i in range(n):
    input_data=input().split()
    array.append((input_data[0], int(input_data[1]))) #튜플로 넣기

#람다설치가 안됨
array=sorted(array,key=lamda student:student[1])

for student in array:
    print(student[0],end=' ')
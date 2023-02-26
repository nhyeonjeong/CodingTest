n,m=map(int,input().split())
#내코드
# max=0
# for i in range(n):
#     numbers=list(map(int, input().split()))
#     numbers.sort()
#     if max<numbers[0]:
#         max=numbers[0]
# print(max)

#min 함수 사용
result=0
for i in range(n):
    data=list(map(int,input().split()))
    min_value=min(data)
    result=min(min_value,result)

print(result)
n,m,k=map(int, input().split())
numbers=list(map(int, input().split())) #배열입력받기
numbers.sort()
bb=numbers[-1] #배열에서 제일 큰 수
b=numbers[-2] #배열에서 그 다음으로 큰 수

rot=m//(k+1) #(제일 큰 수*k + 그 다음으로 큰 수)가 몇 번 나올 수 있는지
rot2=m%(k+1) #위의 나머지
sum=rot*(bb*k+b)+rot2*bb
print(sum)




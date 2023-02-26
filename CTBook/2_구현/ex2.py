n=int(input())
#3이 한번이라도 포한되는 경우의 수 출력

#삼중지문 사용...
cnt=0
for hour in range(n+1):
    for minute in range(0,60):
        for second in range(0,60):
            if '3' in str(hour)+str(minute)+str(second):
                cnt+=1

print(cnt)

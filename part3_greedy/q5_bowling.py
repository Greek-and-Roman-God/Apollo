# Q5 볼링공 고르기
info = list(map(int, input().split(' ')))
ball = list(map(int, input().split(' ')))

result = 0
for i1 in range(0,info[0]):
    temp = ball[i1+1:]
    result = result + len(temp) - temp.count(ball[i1])

print(result)

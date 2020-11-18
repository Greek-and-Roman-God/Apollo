# OX퀴즈

#1
cnt = int(input())
datas = []
for _ in range(cnt):
    datas.append(input())

for data in datas:
    score = 0
    temp = 0
    for d in data:
        if d == 'O':
            temp += 1
            score += temp
        elif d == 'X':
            temp = 0
    print(score)

#2
cnt = int(input())
datas = []
for _ in range(cnt):
    datas.append(input())

for data in datas:
    score = 0
    temp = 1
    for d in data:
        if d == 'X':
            score += temp
            temp = 1
        else:
            temp += 1
    print(score)
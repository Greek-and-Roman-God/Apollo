# OX퀴즈

cnt = int(input())
datas = []
for _ in range(cnt):
    datas.append(input())

for data in datas:
    score = 0
    temp = 0
    for d in data:
        # x면 temp를 0으로 만들기
        # temp의 초기값은 1
        if d == 'O':
            temp += 1
            score += temp
        elif d == 'X':
            temp = 0
    print(score)

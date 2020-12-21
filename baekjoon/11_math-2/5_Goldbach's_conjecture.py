# 9020번 골드바흐의 추측
# https://www.acmicpc.net/problem/9020
limit = 6000
template = [1]*(limit+1)
template[0] = template[1] = 0
for num in range(2, limit//2+1):
    if template[num]:
        for i in range(num*2, limit, num):
            template[i] = 0

t = int(input())

for _ in range(t):
    n = int(input())

    num = n//2

    while 1:
        # print(f'{num} {n-num}')
        if template[num] and template[n-num]:
            break
        num -= 1

    print(num, n-num)

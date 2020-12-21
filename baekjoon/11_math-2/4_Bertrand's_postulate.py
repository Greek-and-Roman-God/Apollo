# 4948 베르트랑 공준
# https://www.acmicpc.net/problem/4948
n = 123456
temp = [1] * (2*n+1)
temp[0] = temp[1] = 0
for i in range(2, n//2+1):
    for j in range(i*2, n*2+2, i):
        if temp[j]:
            temp[j] = 0

while True:
    cnt = 0
    n = int(input())
    if n == 0:
        break

    cnt = temp[n+1:2*n+1].count(1)
    print(cnt)

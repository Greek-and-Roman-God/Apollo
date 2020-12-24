# 1436 영화감독 숍
# https://www.acmicpc.net/problem/1436

n = int(input())
i = 665
cnt = 0
while 1:

    i += 1
    if '666' in str(i):
        cnt += 1
    if n == cnt:
        break
print(i)

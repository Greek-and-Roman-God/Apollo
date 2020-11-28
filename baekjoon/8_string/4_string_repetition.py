# 2675 문자열 반복
# https://www.acmicpc.net/problem/2675
cnt = int(input())

for _ in range(cnt):
    r, s = input().split()

    result = ''
    for char in s:
        result += char * int(r)
    print(result)

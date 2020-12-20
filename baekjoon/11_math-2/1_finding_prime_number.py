# 1978 소수 찾기
# https://www.acmicpc.net/problem/1978

n = int(input())
cnt = 0
nums = list(map(int, input().split()))


for num in nums:
    if num == 1:
        continue
    for i in range(2, num//2+1):
        if num % i == 0:
            break
    else:
        cnt += 1

print(cnt)

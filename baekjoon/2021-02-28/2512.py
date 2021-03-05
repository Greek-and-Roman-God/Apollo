# 예산
# https://www.acmicpc.net/problem/2512
n = int(input())
needs = list(map(int, input().split()))
total = int(input())

start = 1
end = max(needs)
result = 0
while start <= end:
    mid = (start + end) // 2
    temp_total = sum([mid if mid < need else need for need in needs])

    if temp_total > total:
        end = mid - 1
    else:
        start = mid + 1
        result = mid
print(result)

# 랜선 자르기
# https://www.acmicpc.net/problem/1654

k, n = map(int, input().split())
lans = []
for _ in range(k):
    lans.append(int(input()))
start = 1
end = max(lans)
result = 0
while start <= end:
    mid = (start + end) // 2
    cnt = sum([lan // mid for lan in lans])

    if cnt >= n:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
print(result)

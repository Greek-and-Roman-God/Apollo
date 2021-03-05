# 로프
# https://www.acmicpc.net/problem/2217
n = int(input())
roops = []
for _ in range(n):
    roops.append(int(input()))

roops.sort(reverse=True)
result = roops[0]

for i in range(2, n+1):
    if result < roops[i-1] * i:
        result = roops[i-1] * i

print(result)

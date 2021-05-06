# 치킨배달
# 백준
from itertools import combinations
n, m = map(int, input().split())

house = []
chicken = []

for i in range(n):
    row = input().split()
    for j, r in enumerate(row):
        if r == "0":
            continue
        elif r == "1":
            house.append([i+1, j+1])
        elif r == "2":
            chicken.append([i+1, j+1])

combi = list(combinations(chicken, m))
# print(combi)
answer = (2 * n) * (2*n)

for com in combi:
    temp = 0
    for h in house:
        hx, hy = h
        dist = 2*n + 1
        for c in com:
            cx, cy = c
            dist = min(dist, abs(hx-cx)+abs(hy-cy))
        # print(dist)
        temp += dist
    answer = min(answer, temp)
print(answer)

# 초기값을 잘 계산해서 줘야함

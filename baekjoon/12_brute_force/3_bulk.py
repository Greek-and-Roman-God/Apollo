# 7568 덩치
# https://www.acmicpc.net/problem/7568
n = int(input())
bulks = []
for _ in range(n):
    bulk = list(map(int, input().split()))
    bulks.append(bulk)

for i, b in enumerate(bulks):
    rank = 0
    for u in bulks:
        if u[0] > b[0] and u[1] > b[1]:
            rank += 1
    else:
        print(rank+1, end=" ")

# 14720 우유 축제
# https://www.acmicpc.net/problem/14720

# 딸기0 -> 초코1 -> 바나나2 -> 딸기

n = int(input())

stores = list(map(int, input().split()))

drink = 0
i = 0
for store in stores:
    if i % 3 == store:
        drink += 1
        i += 1
print(drink)

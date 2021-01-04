# 5585 거스름돈
# https://www.acmicpc.net/problem/5585

price = int(input())
charge = 1000 - price
coins = [500, 100, 50, 10, 5, 1]
cnt = 0
for coin in coins:
    cnt += charge // coin
    charge %= coin
print(cnt)

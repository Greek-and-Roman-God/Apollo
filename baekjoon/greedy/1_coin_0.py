# 동전 0
# https://www.acmicpc.net/problem/11047

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coin = int(input())
    coins.append(coin)

coins.sort(reverse=True)
i = 0
cnt = 0
while 1:
    if k // coins[i] != 0:
        # print(f'coins[{i}] {coins[i]} k {k}')
        cnt += k // coins[i]
        k = k % coins[i]
    if k == 0:
        print(cnt)
        break
    i += 1

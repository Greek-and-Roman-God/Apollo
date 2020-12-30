# 2798 블랙잭
# https://www.acmicpc.net/problem/2798
n, m = map(int, input().split())

cards = list(map(int, input().split()))

temp = []

for i, c in enumerate(cards):
    for j, a in enumerate(cards[i+1:]):
        for r in cards[i+1+j+1:]:
            print(f'c,a,r {c, a, r}')
            num = c+a+r
            if num > m:
                continue
            else:
                temp.append(num)
print(max(temp))


# 2
n, m = map(int, input().split())

cards = list(map(int, input().split()))

temp = 0

for i, c in enumerate(cards):
    for j, a in enumerate(cards[i+1:]):
        for r in cards[i+1+j+1:]:
            print(f'c,a,r {c, a, r}')
            num = c+a+r
            if num > m:
                continue
            else:
                if temp < num:
                    temp = num
print(temp)

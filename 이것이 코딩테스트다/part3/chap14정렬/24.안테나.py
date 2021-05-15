# 안테나
# https://www.acmicpc.net/problem/18310
from math import ceil
n = int(input())
houses = list(map(int, input().split()))

# 1 =================================================
# avr = sum(houses) / n

# houses.sort(key=lambda x: abs(x-avr))
# print(houses[0])

# 2 =================================================
# result = []
# for loc in range(min(houses), max(houses)+1:
#     temp = 0
#     for h in houses:
#         temp += abs(loc - h)
#     result.append((temp, loc))
# result.sort()
# print(result[0][1])


# 3 =================================================
houses.sort()
print(houses[n//2-1])

# 중간위치에 안테나를 설치하면 모든 거리의 합이 최소가 나옴

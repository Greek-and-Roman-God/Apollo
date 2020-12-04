# 2869 달팽이는 올라가고 싶다
from math import ceil
A,B,V = map(int, input().split())
# 마지막날은 올라가는 게 끝 -> (높이 - 올라감)까지 얼마나 걸리는지 계산 (올라감 - 내려감)으로 나눠줌
# 계산 후 마지막날 올라가야 끝이니까 + 1
day = ceil((V - A) / (A - B)) + 1
print(day)
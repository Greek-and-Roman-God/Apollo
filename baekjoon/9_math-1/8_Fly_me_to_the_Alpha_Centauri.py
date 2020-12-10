# 1011 Fly me to the Alpha Centauri
# https://www.acmicpc.net/problem/1011
from math import ceil

T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    temp = 0
    i = 0
    dist = y - x

    while temp < dist:
        i += 1
        temp += 2*i
        # print(f'i = {i}, temp = {temp}')

    if temp - dist < i:
        print(i * 2)
    else:
        print(i * 2 - 1)

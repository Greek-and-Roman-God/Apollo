# 1037 약수
# https://www.acmicpc.net/problem/1037
n = int(input())
measures = list(map(int, input().split()))
measures.sort()
print(measures[0] * measures[-1])

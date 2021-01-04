# 1434 책 정리
# https://www.acmicpc.net/problem/1434
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(sum(a) - sum(b))

# 15650 N&M(2)
# https://www.acmicpc.net/problem/15650
from itertools import combinations

n, m = map(int, input().split())
num_list = ''.join([str(num) for num in range(1, n+1)])
# print(num_list)
result = list(combinations(num_list, m))
for r in result:
    print(' '.join(r))

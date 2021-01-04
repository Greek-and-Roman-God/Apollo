# 15649 N&M(1)
# https://www.acmicpc.net/problem/15649
from itertools import permutations

n, m = map(int, input().split())
num_list = ''.join([str(num) for num in range(1, n+1)])
# print(num_list)
result = list(permutations(num_list, m))
for r in result:
    print(' '.join(r))

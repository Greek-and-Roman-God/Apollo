# 2485 가로수
# https://www.acmicpc.net/problem/2485
# import math
import sys
n = int(sys.stdin.readline().strip())

tree_dists = []
pre = int(sys.stdin.readline().strip())
first = pre
for _ in range(n-1):
    next_num = int(sys.stdin.readline().strip())
    tree_dists.append(next_num-pre)
    pre = next_num
last = next_num


def gcd(a, b):
    result = 0
    if a > b:
        a, b = b, a

    while b > 0:
        result = b
        a, b = b, a % b
    return result

# pop이 느렸음
# pre_gcd = gcd(tree_dists.pop(0), tree_dists.pop(0))
# while tree_dists:
#     num = tree_dists.pop(0)
#     pre_gcd = gcd(pre_gcd, num)


pre = gcd(tree_dists[0], tree_dists[1])
for i in range(2, n-1):
    pre = gcd(pre, tree_dists[i])

print((last-first)//pre-1-(n-2))

# 다른 사람 풀이
# 보이는 대로 풀었는데 빠르네...

# N = int(input())
# trees = []
# for _ in range(N):
#     trees.append(int(sys.stdin.readline()))

# dist = []
# for i in range(N-1):
#     dist.append(trees[i+1] - trees[i])

# interval = dist[0]
# for i in dist:
#     interval = math.gcd(interval, i)

# cnt = 0
# for i in dist:
#     cnt += i // interval - 1

# print(cnt)

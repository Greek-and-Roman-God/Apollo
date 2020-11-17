# 나무 자르기
from math import ceil

n, need=map(int,input().split())
tree_h = list(map(int,input().split()))

tree_h.sort()
tree_h.reverse()

print(tree_h)


i = 0
count = 1
log = 0
while 1:
    log += (tree_h[i] - tree_h[i+1])*count
    if log >= need:
        # tree_h[i] > answer > tree_h[i+1]
        answer = tree_h[i] - ceil((log - need)/count) if log != need else tree_h[i+1]
        break
    i += 1
    count += 1

print(answer)

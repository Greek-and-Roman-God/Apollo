# 행성터널

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
parent = [0] * (n + 1)

edges = []
result = 0

for i in range(1, n+1):
    parent[i] = i

pos = []
for _ in range(n):
    x, y, z = map(int, input().split())
    pos.append([x, y, z])

for i in range(1, n):
    for j in range(i+1, n):
        edges.append((min(abs(pos[i][0] - pos[j][0]), abs(pos[i]
                                                          [1] - pos[j][1]), abs(pos[i][2] - pos[j][2])), i, j))
print(edges)
edges.sort()
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(cost)

# 탑승구

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


gates = int(input())
plane = int(input())
parent = [0] * (gates+1)

for i in range(gates+1):
    parent[i] = i

result = 0

for _ in range(plane):
    root = find_parent(parent, int(input()))
    if root != 0:
        union_parent(parent, root, root-1)
        result += 1

print(result)

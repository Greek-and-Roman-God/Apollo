# 도시 분할 계획
def find_parent(parent, x):
    # 루트노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [0] * (n+1)

edges = []
result = 0

for i in range(1, n+1):
    parent[i] = i

for _ in range(m):
    a, b, cost = map(int, input().split())
    # 비용손우로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()
last = 0  # 최소 신장 트리에 포함되는 간성 중 가장 비용이 큰 간선

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost

print(result - last)

# 2021-10-02

n, m = map(int, input().split())
parent = [0] * (n+1)

edges = []
result = 0

for i in range(1, n+1):
    parent[i] = i

for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 비용을 기준으로 간선을 정렬함
# 마을을 두 개로 나누려면 간선 하나를 제거
# 문제에서 비용의 합의 최솟값을 구하라고 했으므로
# 가장 비싼 간선을 제거
edges.sort()
last = 0

# 모든 집들을 연결함
for edge in edges:
    cost, a, b = edge
    # a와 b 사이를 이동할 수 없다면
    if find_parent(parent, a) != find_parent(parent, b):
        # 도로를 연결
        union_parent(parent, a, b)
        # 도로의 비용을 저장
        result += cost
        # 가장 마지막에 도로의 비용(제일 비싼 도로)을 저장
        last = cost
    # 아니라면 패스

# 모든 도로의 비용에서 가장 마지막에 연결된 도로의 비용을 제한게 결과
print(result - last)

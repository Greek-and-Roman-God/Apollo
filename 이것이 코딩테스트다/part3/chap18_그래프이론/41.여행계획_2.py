# 여행계획

# 부모 찾기
# 부모가 저장되어 있는 리스트에서 검색
# 트리의 부모는 자기 자신을 부모로 가리키고 있으므로
# 자기 자신을 가리키고 있는 요소를 만날 때까지 재귀를 돔
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]

# a와 b 트리를 합침
# 부모는 a와 b의 부모를 비교해서 정함


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [0] * (n + 1)

for i in range:
    parent[i] = i

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        # 연결 되어 있다면
        if data[i] == 1:
            # 트리를 합치고 새로운 부모를 정해줌
            union_parent(parent, i+1, j+1)

plan = list(map(int, input().split()))

result = True
for i in range(m-1):
    # 순서대로 두 도시씩 골라서 둘이 같은 트리인지 확인함
    # 같은 트리가 아니라면 여행할 수 없는 루트임
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i+1]):
        result = False

if result:
    print("YES")
else:
    print("NO")

# 팀 결성
# 2021-09-05
def find_parent(parent, x):
    # 루트 노드가 아니면 루트노드를 찾을 때까지 재귀 호출
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


n, m = map(int, input().split())
parent = [0] * (n+1)  # 부모 테이블 초기화

# 부모를 자기자신으로 세팅
for i in range(n+1):
    parent[i] = i

# 연산
for i in range(m):
    oper, a, b = map(int, input().split())

    # union 연산
    if oper == 0:
        union_parent(parent, a, b)
    elif oper == 1:  # find 연산
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")

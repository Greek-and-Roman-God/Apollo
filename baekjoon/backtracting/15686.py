# 15686 치킨배달
# https://www.acmicpc.net/problem/15686
n, m = map(int, input().split())

chickens = []       # 치킨 집의 위치를 저장
houses = []         # 집 위치를 저장
for i in range(n):
    data = list(map(int, input().split()))

    for j in range(n):
        if data[j] == 2:
            chickens.append((i, j))
        elif data[j] == 1:
            houses.append((i, j))


checked = [0] * len(chickens)


def chk_dist(checked):
    dists = 0
    for hou_x, hou_y in houses:
        dist = 1000000000
        for ind, (chi_x, chi_y) in enumerate(chickens):
            if checked[ind] == 1:
                # 저장된 최소 거리와 지금 거리를 비교
                dist = min(dist, abs(chi_x-hou_x) + abs(chi_y-hou_y))
        dists += dist
    return dists


min_dist = 0
dists = []


def dfs(i, start):
    global min_dist

    if i == m:
        min_dist = chk_dist(checked)
        dists.append(min_dist)
        return

    for ind in range(start, len(chickens)):
        if checked[ind] == 0:
            checked[ind] = 1
            dfs(i+1, ind)
            checked[ind] = 0


dfs(0, 0)
print(min(dists))

# 치킨집과 집의 좌표를 따로 저장
# 치킨집을 m만큼 고르는 조합을 dfs로 구한다.
# 치킨집을 m개 골랐을 때 집과 치킨집들 사이의 거리를 계산해서 제일 가까운 치킨집의 거리를 치킨 거리에 저장함
# 모든 조합에서 치킨 거리를 계산하고 그 중 제일 작은 치킨 거리를 출력

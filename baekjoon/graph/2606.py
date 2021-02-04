# 2606 바이러스
# https://www.acmicpc.net/problem/2606
from collections import deque
number = int(input())
links_number = int(input())

network = [[0] * (number+1) for _ in range(number+1)]

for _ in range(links_number):
    i, j = map(int, input().split())
    network[i][j] = 1
    network[j][i] = 1


def bfs(i):
    queue = deque()
    queue.append(i)
    zombie = []
    while queue:
        parent = queue.popleft()
        for i, link in enumerate(network[parent]):
            if link and i not in zombie:    # 중복된 링크를 방문하지 않기 위해 zombie 리스트를 만들어줌
                network[parent][i] = 0
                network[i][parent] = 0
                queue.append(i)
                zombie.append(i)
    return zombie


print(len(bfs(1)))

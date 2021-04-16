# 커리큘럼
from collections import deque
import copy
v = int(input())

indegree = [0] * (v+1)
graph = [[] for _ in range(v+1)]
time = [0] * (v+1)

for i in range(1, v+1):
    temp = list(map(int, input().split()))
    time[i] = temp[0]
    for x in temp[1:-1]:
        indegree[i] += 1
        graph[x].append(i)
print("indegree: ", indegree)
print("time: ", time)
print("graph: ", graph)


def topology_sort():
    result = copy.deepcopy(time)    # 알고리즘 수행 결과를 담을 리스트
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()

        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)
    for i in range(1, v + 1):
        print(result[i])


topology_sort()

# 1697 숨바꼭질
# https://www.acmicpc.net/problem/1697

# 시간초과
# n, k = map(int, input().split())

# points = [n]
# i = 0
# step = 1
# cnt = 0
# while k not in points:
#     num = points.pop(0)
#     points.append(num-1)
#     points.append(num+1)
#     points.append(num*2)

#     if len(points) > i:
#         step *= 3
#         i += step
#         cnt += 1

# print(cnt)


n, k = map(int, input().split())
times = [0] * 100001
q = [n]
while q:
    point = q.pop(0)
    if point == k:
        print(times[point])
        break
    for next_point in (point+1, point-1, point*2):
        if 0 <= next_point < 100001 and not times[next_point]:
            times[next_point] = times[point] + 1
            q.append(next_point)

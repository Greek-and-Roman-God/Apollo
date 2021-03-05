# 나무 자르기
# https://www.acmicpc.net/problem/2805

n, m = map(int, input().split())
logs = list(map(int, input().split()))


# def check(h):
#     cut = sum([log-h if log-h > 0 else 0 for log in logs])
#     rest = sum([1 if log-h <= 0 else 0 for log in logs])
#     return cut, rest


# h = max(logs)
# while True:
#     cut, rest = check(h)
#     # print(h, cut, rest)
#     if m <= cut < m + n:
#         result = h
#         break
#     elif cut < m:
#         # print("너무 적게 잘랐으니까 높이를 줄이자")
#         if h // 2 == 0:
#             h -= 1
#         else:
#             h = h // 2
#     else:
#         # print("너무 많이 잘랐으니/까 높이를 늘이자")
#         if (logs[-1] - h) // 2 == 0:
#             h += 1
#         else:
#             h += (logs[-1] - h) // 2
# print(result)

start = 0
end = max(logs)

while start <= end:
    mid = (start+end) // 2
    cut = sum([log-mid if log - mid > 0 else 0 for log in logs])

    if cut >= m:
        start = mid + 1
        h = mid
    else:
        end = mid - 1
print(h)

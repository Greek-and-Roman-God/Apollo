# 1085 직사각형에서 탈출
# https://www.acmicpc.net/problem/1085

x, y, w, h = map(int, input().split())
dist1 = w - x if w - x <= w//2 else x
dist2 = h - y if h - y <= h//2 else y
# print(f'dist1 {dist1} dist2 {dist2}')
print(dist1 if dist1 < dist2 else dist2)

# 2 속도 별 차이 없음, 그때그때 서버 상태에 따라 속도가 다르게 찍히나보다
dist = [x, y, w-x, h-y]
print(min(dist))

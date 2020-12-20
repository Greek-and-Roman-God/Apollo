# 3009 네 번쨰 점
# https://www.acmicpc.net/problem/3009

# 직사각형은 꼭짓점의 각이 전부 직각이어야하기 떄문에
# x축에 수평인 직선 2개와 y축에 수평인 직선 두개로 이루어져 있음
# 때문에 접점 4개의 좌표는 동일한 좌표가 x,y에서 각각 두번씩 나오게됨
# (딘, 기울어져 있는 직사각형은 제외) -> 통과한걸보니 고려하지 않은듯

# 두번 나오지 않는 수(한번 나온 수)를 4번째 점의 좌표해서 답을 찾을 수 있었음

xs = []
ys = []
for _ in range(3):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)

fourth_dot = [0, 0]

for i in range(3):
    if xs.count(xs[i]) == 1:
        fourth_dot[0] = xs[i]
    if ys.count(ys[i]) == 1:
        fourth_dot[1] = ys[i]

print(fourth_dot[0], fourth_dot[1])

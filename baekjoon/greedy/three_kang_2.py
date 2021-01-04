# 11034 캥거루 세마리2
# https://www.acmicpc.net/problem/11034

# 0    0  0
# 두 마리 사이의 거리가 먼 쪽의 사이로 들어가야함
# 들어간 정수 좌표는 가까운 캥거루의 -1 (어디로 들어가는지는 상관 없음, -1이 중요)
# 1    2  3
# 1과 2의 간격을 구하고 2와 3의 간격을 함
# 1과 2의 간격이 더 넓으니까 3이 1과 2사이로 들어감
# 2    78 -> 5
# 2   67
# 2  56
# 2 45
# 234
while 1:
    try:
        a, b, c = map(int, input().split())
        if b - a > c - b:
            print(b-a-1)
        else:
            print(c-b-1)
    except EOFError:
        break

# 감시 피하기
# https://www.acmicpc.net/problem/18428
# 입력값
n = int(input())
hallway = []
teachers = []
for i in range(n):
    hallway.append(input().split())
    # 선생님 위치는 따로 저장
    for j in range(n):
        if hallway[i][j] == "T":
            teachers.append((i, j))

# answer를 플래그 변수로 사용해서 한번이라도 성공한 경우가 나오면 불필요한 연산은 돌지 않도록 함
answer = False

# dfs 알고리즘을 사용해서 장애물 3개를 설치하는 모든 경우를 계산
# dfs 알고리즘의 결과로 나온 hallway리스트를 확인해서 선생이 볼 수 있는 시야에 학생이 있는지 확인 ( 선생이 한 명이라도 학생을 마주친다면 실패한 경우 )


def dfs(hallway, cnt):
    global answer

    if answer:
        return

    if cnt == 3:
        if check(hallway):
            answer = True
        return

    for i in range(n):
        for j in range(n):
            if hallway[i][j] == "X":
                hallway[i][j] = "O"
                dfs(hallway, cnt + 1)
                hallway[i][j] = "X"


def check(hallway):
    for tx, ty in teachers:
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x = tx + dx
            y = ty + dy

            while 0 <= x < n and 0 <= y < n:
                if hallway[x][y] == "S":
                    return False
                elif hallway[x][y] == "O":
                    break
                x += dx
                y += dy
    return True


dfs(hallway, 0)
if answer:
    print("YES")
else:
    print("NO")

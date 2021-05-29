# 블록 이동하기
# https://programmers.co.kr/learn/courses/30/lessons/60063
from collections import deque
# 1

# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]


# def strai(board, robot, i):
#     global dx, dy
#     (x1, y1), (x2, y2) = robot
#     x1 += dx[i]
#     y1 += dy[i]
#     x2 += dx[i]
#     y2 += dy[i]
#     # print(x1, y1, x2, y2, robot)
#     if board[x1][y1] == 0 and board[x2][y2] == 0:
#         return [(x1, y1), (x2, y2)]
#     return []


# def rotate(board, robot, i):
#     global dx, dy
#     (x1, y1), (x2, y2) = robot
#     if abs(x1-x2) < abs(y1-y2):  # 수평
#         if i > 2:
#             return [[(x1, y1), (x1+dx[i], y1+dy[i])], [(x2, y2), (x2+dx[i], y2+dy[i])]]
#     else:   # 수직
#         if i < 3:
#             return [[(x1, y1), (x1+dx[i], y1+dy[i])], [(x2, y2), (x2+dx[i], y2+dy[i])]]

#     return []


# def check_visit(visited, robot, answer):

#     (x1, y1), (x2, y2) = robot
#     print(visited[x1][y1], visited[x2][y2])
#     if visited[x1][y1] != 0 and visited[x2][y2] != 0 and visited[x1][y1] < answer and visited[x2][y2] < answer:
#         return visited, False

#     visited[x1][y1] = answer+1
#     visited[x2][y2] = answer+1

#     return visited, True


# def solution(board):
#     global dx, dy
#     answer = 0
#     n = len(board)
#     for i in range(len(board)):
#         board[i] = [1] + board[i] + [1]
#     temp = [[1 for i in range(len(board[0]))]]
#     board = temp + board + temp
#     # print(temp, board)
#     robots = deque([[(1, 1), (1, 2)]])
#     # for b in board:
#     #     print(b)

#     visited = {[(1, 1), (1, 2)]}

#     while robots:
#         print(robots)
#         robot = robots.popleft()
#         for v in visited:
#             print(v)
#         (x1, y1), (x2, y2) = robot
#         if (x1, y1) == (n, n) or (x2, y2) == (n, n) or answer == 10:
#             break

#         for i in range(4):
#             move_result = strai(board, robot, i)
#             if move_result:
#                 visited, check_result = check_visit(
#                     visited, move_result, answer)
#                 if check_result:
#                     robots.append(move_result)
#             if (abs(x1 - y1) < abs(x2 - y2) and i >= 2) or (abs(x1 - y1) > abs(x2 - y2) and i < 2):

#                 rotate_result = rotate(board, robot, i)
#                 # print(rotate_result)
#                 if move_result and rotate_result:
#                     for r in rotate_result:
#                         visited, check_result = check_visit(visited, r, answer)
#                         if check_result:
#                             robots.append(r)
#         answer += 1

#     return answer

# 2
def get_next_pos(pos, board):
    next_pos = []   # 반환 결과(이동 가능한 위치들)
    pos = list(pos)  # 현재 위치 정보를 리스트로 변환(집합 -> 리스트)
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    # 상하와주 로 이동하는 경우에 대해서 처리
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        pos1_next_x, pos1_next_y, pos2_next_x, pos2_next_y = \
            pos1_x + dx[i], pos1_y + dy[i], pos2_x + dx[i], pos2_y + dy[i]
        # 이동하고자 하는 두 칸이 모두 비어있다면
        if board[pos1_next_x][pos1_next_y] == 0 and board[pos2_next_x][pos2_next_y] == 0:
            next_pos.append({(pos1_next_x, pos1_next_y),
                             (pos2_next_x, pos2_next_y)})

    # 회전하는 경우
    # 가로
    if pos1_x == pos2_x:
        for i in [-1, 1]:   # 위로 회전하거나, 아래쪽으로 회전
            # 위쪽 혹은 아래쪽 두 칸이 모두 비어있다면
            if board[pos1_x + i][pos1_y] == 0 and board[pos2_x + i][pos2_y] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x + i, pos1_y)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x + i, pos2_y)})
    # 세로
    elif pos1_y == pos2_y:
        for i in [-1, 1]:   # 왼쪽으로 회전하거나, 오른쪽으로 회전
            # 왼쪽 혹은 오른쪽의 두칸이 모두 비어있다면
            if board[pos1_x][pos1_y + i] == 0 and board[pos2_x][pos2_y + i] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y + i)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y + i)})

    # 현재 위치에서 이동할 수 있는 위치를 반환
    return next_pos


def solutions(board):
    # 맵 외곽에 벽을 두는 형태로 맵 변형
    n = len(board)
    new_board = [[1] * (n+2) for _ in range(n+2)]

    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]

    # 너비우선탐색 실행
    q = deque()
    visited = []
    pos = {(1, 1), (1, 2)}  # 시작위치
    q.append((pos, 0))  # 큐에 삽입 후
    visited.append(pos)  # 방문처리

    # 큐가 빌 때까지 반복
    while q:
        pos, cost = q.popleft()
        # (n,n)위치에 로봇이 도달했다면, 최단 거리이므로 반환
        if (n, n) in pos:
            return cost

        # 현재 위치에서 이동할 수 있는 위치 확인
        for next_pos in get_next_pos(pos, new_board):
            # 아직 방문하지 않은 위치라면 큐에 삽입하고 방문처리
            if next_pos not in visited:
                q.append((next_pos, cost + 1))
                visited.append(next_pos)

    return 0

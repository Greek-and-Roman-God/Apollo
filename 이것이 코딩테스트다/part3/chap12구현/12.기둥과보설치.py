# 기둥과 보 설치
# https://programmers.co.kr/learn/courses/30/lessons/60061
from collections import deque

# 1 ========================================================
# 보와 기둥 리스트를 따로 만들어서 풀었음


# def solution(n, build_frame):
#     answer = []

#     dam = [[0]*(n+1) for _ in range(n+1)]
#     column = [[0]*(n+1) for _ in range(n+1)]

#     build_frame = deque(build_frame)

#     def check_column(x, y):
#         if x == 0 or dam[x][y-1] or dam[x][y] or column[x-1][y]:
#             return True
#         return False

#     def check_dam(x, y):
#         # print(f'한쪽이라도 기둥이 있나? {column[x-1][y] or column[x-1][y+1]}')
#         # print(f'보가 양쪽에 다 있나? {dam[x][y-1] or dam[x][y+1]}')
#         if x != 0 and ((column[x-1][y] or column[x-1][y+1]) or (dam[x][y-1] and dam[x][y+1])):
#             return True
#         return False

#     while build_frame:
#         y, x, a, b = build_frame.popleft()
#         print(x, y)
#         if b == 1:
#             if a == 0:  # 기둥
#                 if check_column(x, y):
#                     # print(f'기둥 설치')
#                     column[x][y] = 1
#                 # else:
#                     # print("기둥 설치 무시")
#             else:   # 보
#                 if x != 0 and ((column[x-1][y] or column[x-1][y+1]) or (dam[x][y-1] or dam[x][y+1])):
#                     # print(f'보 설치')
#                     dam[x][y] = 1
#                 # else:
#                     # print("보 설치 무시")
#         else:
#             if column[x][y] == 1:   # 기둥
#                 column[x][y] = 0
#                 # print(
#                 #     f'왼쪽 보 때문에 삭제되면 안됨 {dam[x+1][y-1] and not check_dam(x+1, y-1)}')
#                 # print(
#                 #     f'오른쪽 보 때문에 삭제되면 안됨 {dam[x+1][y] and not check_dam(x+1, y)}')
#                 # print(f'위에 기둥이 있어서 삭제되면 안됨 {column[x][y+1] == 1}')
#                 if (dam[x+1][y] and not check_dam(x+1, y)) or (dam[x+1][y-1] and not check_dam(x+1, y-1)) or column[x][y+1] == 1:
#                     column[x][y] = 1
#                     # print(f'기둥 삭제 무시')
#                 # else:
#                     # print(f'{x} {y} 에 기둥 삭제')

#             else:   # 보
#                 dam[x][y] = 0
#                 # print(f'왼쪽 보의 조건이 맞나? {check_dam(x, y-1)}')
#                 # print(f'오른쪽 보의 조건이 맞나? {check_dam(x, y+1)}')

#                 if not check_dam(x, y-1) or not check_dam(x, y+1):
#                     dam[x][y] = 1
#                     # print(f'보 삭제 무시')

#                 # else:
#                     # print(f'보 삭제')

#     for j, (col, da) in enumerate(zip(column, dam)):
#         for i, (c, d) in enumerate(zip(col, da)):
#             if c == 1:
#                 answer.append([i, j, 0])
#             if d == 1:
#                 answer.append([i, j, 1])
#     answer.sort()
#     return answer


# print(solution(5,	[[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [
#       2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]))
# print(solution(5,	[[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [
#       1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))


# 2 ==================================================
def check(answer):
    for x, y, stuff in answer:
        if stuff == 0:  # 기둥
            # 바닥 위 이거나 y == 0
            # 아래가 기둥 이거나
            # 아래가 보 이거나
            # print(f'{x, y} 체크')
            # print(f'바닥인가? {y == 0}')
            # print(f'아래가 기둥인가? {[x, y-1, 0] in answer}')
            # print(
            #     f'아래가 보의 한쪽 끝인가? {[x-1, y, 1] in answer or [x-1, y-1, 1] in answer}')
            if y == 0 or [x, y, 1] in answer or [x-1, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            return False

        else:   # 보
            # 양쪽이 보 이거나
            # 한쪽이 기둥 이거나
            # 바닥은 노노
            if y != 0 and (([x, y-1, 0] in answer or [x+1, y-1, 0] in answer) or ([x-1, y, 1] in answer and [x+1, y, 1] in answer)):
                continue

            return False

    return True


def solution1(n, build_frame):
    answer = []

    for x, y, stuff, operate in build_frame:
        if operate == 1:
            # print(f'{x, y} 설치')
            answer.append([x, y, stuff])
            if not check(answer):
                # print("설치 취소")
                answer.remove([x, y, stuff])
        else:
            answer.remove([x, y, stuff])
            if not check(answer):
                answer.append([x, y, stuff])
        # print("==================================================")
    return sorted(answer)


# print(solution1(5,	[[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [
#       2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]))
print(solution1(5,	[[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [
      1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))

# 인덱스가 주어진다고 무조건 리스트를 만들어서 풀 필요는 없다
# 리스트를 만들었을 때 더 번거로워질 수 있음
# 문제의 조건을 파악하고 복잡도를 계산하여 풀어야한다.

# 체스판 다시 칠하기
# https://www.acmicpc.net/problem/1018

# n, m = 8, 8
# board = [
#     'WBWBWBWB',
#     'BWBWBWBW',
#     'WBWBWBWB',
#     'BWBBBWBW',
#     'WBWBWBWB',
#     'BWBWBWBW',
#     'WBWBWBWB',
#     'BWBWBWBW',
# ]

# n, m = 10, 13
# board = [

#     'BBBBBBBBWBWBW',
#     'BBBBBBBBBWBWB',
#     'BBBBBBBBWBWBW',
#     'BBBBBBBBBWBWB',
#     'BBBBBBBBWBWBW',
#     'BBBBBBBBBWBWB',
#     'BBBBBBBBWBWBW',
#     'BBBBBBBBBWBWB',
#     'WWWWWWWWWWBWB',
#     'WWWWWWWWWWBWB',
# ]

temp_board = [
    ['WBWBWBWB',
     'BWBWBWBW',
     'WBWBWBWB',
     'BWBWBWBW',
     'WBWBWBWB',
     'BWBWBWBW',
     'WBWBWBWB',
     'BWBWBWBW'],
    ['BWBWBWBW',
     'WBWBWBWB',
     'BWBWBWBW',
     'WBWBWBWB',
     'BWBWBWBW',
     'WBWBWBWB',
     'BWBWBWBW',
     'WBWBWBWB']
]
n, m = map(int, input().split())
board = []
for _ in range(n):
    row = input()
    board.append(row)

temp = 33
for i in range(n-8+1):
    for j in range(m-8+1):
        for t_board in temp_board:
            paint = 0
            for row, temp_row in zip(board[i:i+8], t_board):
                row = row[j:j+8]
                for color, temp_color in zip(row, temp_row):
                    if color != temp_color:
                        paint += 1
            else:
                temp = paint if temp > paint else temp

print(temp)

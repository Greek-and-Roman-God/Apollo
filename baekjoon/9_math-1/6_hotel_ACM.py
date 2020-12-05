# 10250 ACM 호텔

T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())

    room = ''

    floor = N % H if N % H else H
    room_number = N // H if N // H == N / H else N // H + 1
    room = str(floor) + str(room_number).rjust(2,'0')

    print(room)
    




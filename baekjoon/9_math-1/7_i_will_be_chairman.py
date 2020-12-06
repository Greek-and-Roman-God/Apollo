# 2775 부녀회장이 될테야


T = int(input())


for _ in range(T):
    # k층의 n호
    k = int(input())
    n = int(input())
    rooms = [[i for i in range(1,15)]]

    floor = 0

    while 1:
        floor += 1
        n_floor = [1]
        for num in range(1, n):
            temp = n_floor[num-1] + rooms[floor-1][num]
            # print(num, temp)
            n_floor.append(temp)
        rooms.append(n_floor)
        # print(rooms)
        if floor == k:
            print(rooms[k][n-1])
            break
    
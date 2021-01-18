# 6603 로또
# https://www.acmicpc.net/problem/6603

while True:
    input_data = list(map(int, input().split()))
    if input_data[0] == 0:
        break
    k = input_data[0]
    s = input_data[1:]

    selected = [0] * k

    answer = [None] * 6

    def dfs(cnt):
        # print(i, cnt)
        # print(*selected)
        if cnt == 6:
            print(*answer)
            return
        for j in range(k):
            if selected[j] == 0:
                selected[j] = 1
                answer[cnt] = s[j]
                dfs(cnt+1)
                for i in range(j+1, k):
                    selected[i] = 0

    dfs(0)
    print()

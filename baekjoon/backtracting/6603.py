# 6603 로또
# https://www.acmicpc.net/problem/6603

while True:
    input_data = list(map(int, input().split()))
    if input_data[0] == 0:
        break
    k = input_data[0]   # 주어질 숫자 개수
    s = input_data[1:]  # 주어진 숫자들

    selected = [0] * k  # 숫자의 개수만큼의 확인 배열

    answer = [None] * 6  # 뽑을 로또 번호 6개

    def dfs(cnt):
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

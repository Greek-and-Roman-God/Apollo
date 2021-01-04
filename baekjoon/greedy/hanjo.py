# 14659 힌조서열정리하고옴ㅋㅋ
# https://www.acmicpc.net/problem/14659

n = int(input())  # 1 ~ 30000
bongs = list(map(int, input().split()))  # 1~100000 중복x
sorted_bongs = sorted(bongs, reverse=True)
play = 0

for s_bong in sorted_bongs:
    church = 0
    player = bongs.index(s_bong)
    for bong in bongs[player+1:]:
        if s_bong >= bong:
            church += 1
        else:
            break

    if church < play:
        break
    else:
        play = church
print(play)

# 봉이 높을 수록 많은 적을 처치할 수 있으므로 봉이 높은 순으로 얼만큼의 적을 처치할 수 있는지 확인했다.
# 하지만 제일 높은 봉이 제일 많은 적을 처치하는 것은 아니므로(봉의 위치가 예외)
# 그 다음으로 큰 봉이 적 처지 수까지 스캔하여 현재 봉의 처치수가 최댓값이 맞는지 확인했다.
# 다음 봉의 처치수가 현재 봉의 처치수보다 작을 경우 반복을 멈추고 최댓값을 출력한다.

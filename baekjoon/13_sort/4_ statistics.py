# 2108 통계학
# https://www.acmicpc.net/problem/2108
n = int(input())

scores = []
cnt = {}
max_cnt = 0  # 최빈값의 횟수
for _ in range(n):
    score = int(input())
    scores.append(score)

    if score in cnt:
        cnt[score] += 1
    else:
        cnt[score] = 1
    if max_cnt < cnt[score]:
        max_cnt = cnt[score]
scores.sort()


# 산술평균
print(int(round(sum(scores) / float(n), 0)))
# 중앙 값
print(scores[n//2])
# 최빈값
c = 0
freq = []
for key in cnt:
    if cnt[key] == max_cnt:
        freq.append(int(key))
freq = list(set(freq))
if len(freq) > 1:
    freq.sort()
    print(freq[1])
else:
    print(freq[0])

# 범위
print(scores[n-1] - scores[0])

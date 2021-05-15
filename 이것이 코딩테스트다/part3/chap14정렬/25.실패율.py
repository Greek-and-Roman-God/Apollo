# 실패율
# https://programmers.co.kr/learn/courses/30/lessons/42889


def solution(N, stages):
    answer = []
    length = len(stages)
    for i in range(1, N+1):
        cnt = stages.count(i)

        if length == 0:
            fail = 0
        else:
            fail = cnt / length

        answer.append((i, fail))
        length -= i

    answer = sorted(answer, key=lambda t: t[1], reverse=True)

    answer = [i[0] for i in answer]

    return answer

# 문자열 압축
# https://programmers.co.kr/learn/courses/30/lessons/60057
def solution(s):
    answer = len(s)
    # pattern = 1
    for pattern in range(1, len(s)//2+1):
        pre = ""
        result = 0
        cnt = 1
        for i in range(0, len(s), pattern):
            # print(pre, s[i:i+pattern], cnt, result)
            if pre != s[i:i+pattern]:
                pre = s[i:i+pattern]
                result += len(pre)
                if cnt > 1:
                    result += len(str(cnt))
                # print(f'result = {result}')
                cnt = 1
            else:
                cnt += 1
        if cnt > 1:
            result += len(str(cnt))
        # print(result)
        answer = min(answer, result)
    return answer


# answer = solution("aabbaccc")
# print(answer)
# print(solution("ababcdcdababcdcd"))
# print(solution("abcabcdede"))
# print(solution("abcabcabcabcdededededede"))
# print(solution("xababcdcdababcdcd"))
# print(solution("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxz"))
print(solution("zxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"))


# 2021-08-13
def solution2(s):
    answer = len(s)

    for length in range(1, len(s)//2+1):
        pre = ""
        cnt = 1
        result = 0
        for i in range(0, len(s), length):
            if pre != s[i:i+length]:
                pre = s[i:i+length]
                result += len(pre)
                if cnt > 1:
                    result += len(str(cnt))
                cnt = 1
            else:
                cnt += 1
        if cnt > 1:
            result += len(str(cnt))
        answer = min(answer, result)
    return answer

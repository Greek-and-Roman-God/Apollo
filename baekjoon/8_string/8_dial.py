# 5622 다이얼
# https://www.acmicpc.net/problem/5622

phone_num = input()
# 다른 방법으로도 풀 수 있을거같지만
# 문자열이 길어질수록 딕셔너리를 사용하는게 더 효율적일거라고 생각함
dial_dict = {
    'A':2,'B':2,'C':2,
    'D':3,'E':3,'F':3,
    'G':4,'H':4,'I':4,
    'J':5,'K':5,'L':5,
    'M':6,'N':6,'O':6,
    'P':7,'Q':7,'R':7,'S':7,
    'T':8,'U':8,'V':8,
    'W':9,'X':9,'Y':9,'Z':9,
}

answer = 0
for num in phone_num:
    # 걸리는 초 = 숫자+1
    answer += dial_dict[num]+1
print(answer)
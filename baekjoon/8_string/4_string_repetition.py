# 2675 문자열 반복
# https://www.acmicpc.net/problem/2675
cnt = int(input())

# 입력받은 cnt 만큼 r(몇 번 반복할지)과 s(문자열)를 입력받음
for _ in range(cnt):
    r, s = input().split()

    # - 결과값을 담을 빈 문자열
    #   1. 새로운 r, s를 받을 때마다 초기회시켜줘야하기 때문에 r,s의 다음으로 실행된다.
    result = '' 

    # - 입력받은 문자열 s의 문자들을 앞에서부터 하나씩 꺼내 사용하기 위해 for in을 사용하여 반복문을 돌림
    #   1. s에서 가져온 char를 r번 반복하여 result에 순서대로 이어붙인다.
    for char in s:
        result += char * int(r)
    print(result)

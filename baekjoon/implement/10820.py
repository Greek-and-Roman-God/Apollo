# 10820 문자열 분석
# https://www.acmicpc.net/problem/10820

while True:
    try:
        string = input()
        result = [0, 0, 0, 0]
        for ch in string:
            num = ord(ch)
            if 97 <= num <= 122:
                result[0] += 1
            if 65 <= num <= 90:
                result[1] += 1
            if 48 <= num <= 57:
                result[2] += 1
            if num == 32:
                result[3] += 1
        print(' '.join(list(map(str, result))))
    except EOFError:
        break

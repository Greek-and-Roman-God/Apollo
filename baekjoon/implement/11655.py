# 11655 ROT13
# https://www.acmicpc.net/problem/11655


string = input()
result = ''
for s in string:
    num = ord(s)
    if 97 <= num <= 122:
        result += chr(((num-97+13) % 26) + 97)
        continue
    if 65 <= num <= 90:
        result += chr(((num-65+13) % 26) + 65)
        continue
    result += s
print(result)

# 11656 접미사 배열
# https://www.acmicpc.net/problem/11656

word = input()
result = []
for i in range(len(word)):
    result.append(word[i:])
result.sort()
for r in result:
    print(r)

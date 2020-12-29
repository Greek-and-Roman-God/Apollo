# 1181 단어 정렬
# https://www.acmicpc.net/problem/1181
n = int(input())
words = []
for _ in range(n):
    word = input()
    words.append(word)

# words = [
#     'but',
#     'i',
#     'wont',
#     'hesitate',
#     'no',
#     'more',
#     'no',
#     'more',
#     'it',
#     'cannot',
#     'wait',
#     'im',
#     'yours',
# ]
words = list(set(words))
words.sort()
words.sort(key=lambda x: len(x))

for word in words:
    print(word)

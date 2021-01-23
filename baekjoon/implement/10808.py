# 10808 알파벳 개수
# https://www.acmicpc.net/problem/10808
word = input()

alphas = [0] * 26

for alpha in word:
    alphas[ord(alpha)-97] += 1

print(' '.join(list(map(str, alphas))))

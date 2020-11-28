# 10809 알파벳 찾기
# https://www.acmicpc.net/problem/10809

'''

>>> import string
>>> string.ascii_lowercase[:14]
'abcdefghijklmn'
>>> string.ascii_lowercase[:14:2]
'acegikm'

for i in range(ord('a'), ord('n')+1):
    print chr(i),
'''

word = input()

for i in range(ord('a'), ord('z')+1):
    print(word.find(chr(i)), end=' ')
print()

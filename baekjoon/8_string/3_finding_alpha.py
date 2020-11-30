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

# - 입력받은 문자에 a ~ z까지의 문자가 어디에 존재하는지 계산하기 위해 반복문 사용
#   1. a ~ z까지의 문자를 아스키코드로 변경하여 반복문에 사용
#   2. 아스키코드로 바꾼 숫자들을 다시 문자로 바꾼 후 문자열 내장함수 find를 사용하여 각각 어디에 최초로 등장하는지 출력
#   3. find함수는 문자가 존재하지 않을 경우 -1을 반환한다. (비슷한 기능을 하는 index함수는 문자가 존재하지 않을 경우 예외를 발생시킴)
for i in range(ord('a'), ord('z')+1):
    print(word.find(chr(i)), end=' ')
print()

# 2941 크로아티아 알파벳
# https://www.acmicpc.net/problem/2941

word = input()

# alpha = {
#     'c=':'č',
#     'c-':'ć',
#     'dz=':'dž',
#     'd-':'đ',
#     'lj':'lj',
#     'nj':'nj',
#     's=':'š',
#     'z=':'ž',
# }
alpha = ['c=','c-','dz=','d-','lj','nj','s=','z=']
cnt = 0
# for key in alpha.keys():
for key in alpha:

    cnt += word.count(key) # key와 일치하는 문자열의 개수를 구함
    word = word.replace(key, ' ') # ' '으로 replace, ''로 replace할 경우 또 다른 크로아티아 문자와 일치할 수 있음

    print(f'key {key} word {word}')
# 체크하면서 ' '로 채워넣은 부분을 ''으로 replace
# 남은 부분은 문제 조건에 따라 문자 하나하나가 크로아티아 알파벳이므로 len으로 그 개수를 셀 수 있다.
word = word.replace(' ','') 

# for에서 구한 cnt와 word의 길이로 결과를 출력
print(cnt+len(word))


# 정리
word = input()

alpha = ['c=','c-','dz=','d-','lj','nj','s=','z=']
cnt = 0
for key in alpha:
    word += word.replace(key, '*')

print(len(word))

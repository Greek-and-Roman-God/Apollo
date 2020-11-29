# 2941 크로아티아 알파벳
# https://www.acmicpc.net/problem/2941

word = input()

alpha = {
    'c=':'č',
    'c-':'ć',
    'dz=':'dž',
    'd-':'đ',
    'lj':'lj',
    'nj':'nj',
    's=':'š',
    'z=':'ž',
}
alpha = ['c=','c-','dz=','d-','lj','nj','s=','z=']
cnt = 0
# for key in alpha.keys():
for key in alpha:

    cnt += word.count(key)
    word = word.replace(key, ' ')
    print(f'key {key} word {word}')
word = word.replace(' ','')
print(cnt+len(word))

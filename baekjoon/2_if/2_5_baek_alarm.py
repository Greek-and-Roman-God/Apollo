# 알람시계
h,m=map(int,input().split(' '))
if m-45>=0: m=m-45
elif h-1<0: 
    h=24+h-1
    m=60+m-45
else: 
    h=h-1
    m=60+m-45
print(f'{h} {m}')
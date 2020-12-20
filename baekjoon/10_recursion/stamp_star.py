# 2447 별 찍기 - 10
# https://www.acmicpc.net/problem/2447


def stars(star):
    matrix = []
    for i in range(3 * len(star)):  # range(9)

        if i // len(star) == 1:
            matrix.append(star[i % len(star)] + " " *
                          len(star) + star[i % len(star)])
            # 3 "***" + "   " + "***"
            # 4 "* *" + "   " + "* *"
            # 5 "***" + "   " + "***"
        else:
            matrix.append(star[i % len(star)] * 3)
            # 0, 6 "***"*3 -> *********
            # 1, 7 "* *"*3 -> * ** ** *
            # 2, 8 "***"*3 -> *********
    return list(matrix)


star = ["***", "* *", "***"]
n = int(input())
k = 0

while n != 3:
    n = int(n / 3)
    k += 1

for i in range(k):
    star = stars(star)
for i in star:
    print(i)

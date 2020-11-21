# 정수 N개의 합
# 통과
def solve(a: int) -> int:
    return sum(a)

# 런타임에러
def solve(a: int) -> int:

    result = 0

    for num in a:
        result += a

    return result
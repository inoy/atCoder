import math

N = int(input())
A = list(map(int, input().split()[:N]))

a = A.pop(0)
# 最小公倍数 LeastCommonMultiple
lcm = a
while len(A) > 0:
    b = A.pop(0)
    # 最大公約数 GreatestCommonDivisor
    gcd = math.gcd(a, b)
    lcm = int(lcm * b / gcd)

    a = lcm
print(int(lcm))

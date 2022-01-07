N = int(input())
A = list(map(int, input().split()[:N]))

a = A.pop(0)

while len(A) > 0:
    b = A.pop(0)

    while a > 0 and b > 0:
        if a > b:
            a = a % b
        else:
            b = b % a
        if a < b:
            a = b
print(a) if a > b else print(b)

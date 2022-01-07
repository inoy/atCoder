N = int(input())

for n in range(2, N + 1):
    a = 0
    for i in range(2, n):
        if n % i == 0:
            a = n
            break
    if a == 0:
        print(n, end=" ")

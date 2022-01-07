N, X, Y = map(int, input().split())

a = 0
for n in range(1, N + 1):
    if n % X == 0 or n % Y == 0:
        a += 1
print(a)

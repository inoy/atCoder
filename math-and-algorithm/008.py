N, S = map(int, input().split())

a = 0
for red in range(1, N + 1):
    for blue in range(1, N + 1):
        if (red + blue) <= S:
            a += 1
print(a)

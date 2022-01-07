N = int(input())

a = list()
for n in range(2, int(N ** 0.5) + 1):
    while N % n == 0:
        N /= n
        a.append(n)
if N >= 2:
    a.append(int(N))
print(*a)

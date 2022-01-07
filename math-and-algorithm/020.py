N = int(input())
A = list(map(int, input().split()[:N]))

count = 0
for a in range(0, N):
    for b in range(a + 1, N):
        for c in range(b + 1, N):
            for d in range(c + 1, N):
                for e in range(d + 1, N):
                    if A[a] + A[b] + A[c] + A[d] + A[e] == 1000:
                        count += 1
print(count)

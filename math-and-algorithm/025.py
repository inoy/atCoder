N = int(input())
A = list(map(int, input().split()[:N]))
B = list(map(int, input().split()[:N]))

perA = 2 / 6
perB = 4 / 6
ans = 0
for n in range(N):
    ans += (A[n] * perA) + (B[n] * perB)
print(ans)

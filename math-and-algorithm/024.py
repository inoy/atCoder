N = int(input())
P = [map(int, input().split()[:2]) for _ in range(N)]

ans = 0
for p, q in P:
    ans += q / p
print(ans)

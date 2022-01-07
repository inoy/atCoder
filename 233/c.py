import sys

input = sys.stdin.readline

N, X = map(int, input().split())
DP = {1: 1}

for i in range(N):
    A = list(map(int, input().split()))
    NDP = dict()

    for dp in DP:
        for a in A[1:]:
            if dp * a in NDP:
                NDP[dp * a] += DP[dp]
            else:
                NDP[dp * a] = DP[dp]
    DP = NDP

# DP = {10: 1, 5: 1, 80: 1, 40: 2, 20: 1}
# Keyが総乗, Valueが数
if X in DP:
    print(DP[X])
else:
    print(0)

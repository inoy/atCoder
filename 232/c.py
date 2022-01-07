N, M = map(int, input().split())
A = [[False] * N for _ in range(N)]
C = [[False] * N for _ in range(N)]

for _ in range(M):
    U, V = map(int, input().split())
    U -= 1
    V -= 1
    A[U][V] = A[V][U] = True
print(A)

for _ in range(M):
    U, V = map(int, input().split())
    U -= 1
    V -= 1
    C[U][V] = C[V][U] = True
print(C)

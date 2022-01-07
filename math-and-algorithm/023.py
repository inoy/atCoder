N = int(input())
B = list(map(int, input().split()[:N]))
R = list(map(int, input().split()[:N]))

print(
    sum((list(map(lambda b: b / N, B))))
    + sum((list(map(lambda r: r / N, R))))
)

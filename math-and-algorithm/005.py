N = int(input())
A = list(map(int, input().split()[:N]))

print(sum(A) % 100)

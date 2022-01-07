import math

N = int(input())

for i in range(1, math.floor(math.sqrt(N)) + 1):
    if N % i == 0:
        print(i)
        if N / i != i:
            print(int(N / i))

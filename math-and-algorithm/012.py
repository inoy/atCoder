import math

N = int(input())

isNotPrime = False
for i in range(2, math.floor(math.sqrt(N)) + 1):
    if N % i == 0:
        isNotPrime = True
        break
print("No") if isNotPrime else print("Yes")

N = int(input())
A = list(map(int, input().split()[:N]))

aDict = {100: 0, 200: 0, 300: 0, 400: 0}

for a in A:
    aDict[a] += 1

print((aDict[100] * aDict[400]) + (aDict[200] * aDict[300]))

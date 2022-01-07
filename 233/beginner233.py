def a():
    X, Y = map(int, input().split())
    i = 0
    while X + (10 * i) < Y:
        i += 1
    print(i)


def b():
    L, R = map(int, input().split())
    S = input()
    lenS = len(S)  # abcde -> 5
    reversedS = [0] * lenS
    j = 1
    for i in range(lenS):
        if i + 1 < L:
            reversedS[i] = S[i]
        elif R < i + 1:
            reversedS[i] = S[i]
        else:
            reversedS[R - j] = S[i]
            j += 1
    print("".join(reversedS))


# def c():
#     import itertools
#     N, X = map(int, input().split())
#     aSL = [str(input().rstrip('\n')).split()[1:] for _ in range(N)]
#     # print(aS)
#     allNum = list()
#     for aS in aSL:
#         for a in aS:
#             allNum.append(int(a))
#     # print(allNum)
#     allCombination = list()
#     for n in range(1, len(allNum) + 1):
#         for conb in itertools.combinations(allNum, n):
#             # allCombination.append(math.prod(list(conb)))
#             allCombination.append(list(conb))
#     print(allCombination)
#     # print(int(allCombination.count(X) / 2))


def c():
    N, X = map(int, input().split())
    aSL = [str(input().rstrip('\n')).split()[1:] for _ in range(N)]
    allNum = list()
    for aS in aSL:
        print(aS)
        for a in aS:
            print(a)


if __name__ == '__main__':
    # a()
    # b()
    c()

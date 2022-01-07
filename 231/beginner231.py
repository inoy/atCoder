import collections


def a():
    x = int(input())
    print(x / 100)
    pass


def b():
    n = int(input())
    s = [str(input().rstrip('\n')) for _ in range(n)]
    c = collections.Counter(s)
    print(c.most_common()[0][0])


def c():
    N, Q = map(int, input().split())
    A = [(a, 10 ** 9) for a in map(int, input().split())]
    print(f"A = {A}")
    X = []
    for i in range(Q):
        x = int(input())
        X.append((x, i))
    print(f"X = {X}")

    print(f"(A + X) = {(A + X)}")
    AX = sorted(A + X)[::-1]
    print(f"AX = {AX}")

    ans = [0] * Q
    cnt = 0
    print(f"Q = {Q}")
    for x, i in AX:
        print(f"---")
        print(f"x = {x}")
        print(f"i = {i}")
        if i < Q:
            ans[i] = cnt
        else:
            cnt += 1
        print(f"ans = {ans}")
        print(f"cnt = {cnt}")

    print(*ans, sep="\n")


if __name__ == '__main__':
    # a()
    # b()
    c()

def N(): int(input())
def S(): input()


def a():
    v = input()
    iv = int(v)
    if iv >= 42:
        iv += 1
    print("AGC{}".format(str(iv).zfill(3)))


def b():
    t = "oxx" * 1000000
    s = input()
    a = "Yes" if s in t else "No"
    print(a)


def c():
    l1 = input().split()
    l2 = input().split()
    [n, a, b] = map(lambda x: int(x), l1)
    [p, q, r, s] = map(lambda x: int(x), l2)
    fb = c_g(n, a, b)
    # print(fb)
    for gyou in range(q - p + 1):
        for nagasa in range(s - r + 1):
            # print("{},{}  ".format(gyou, nagasa), end="")
            if "{},{}".format(gyou, nagasa) in fb:
                print("#", end="")
            else:
                print(".", end="")
        print()


def c_g(n, a, b):
    arr = []
    max1 = max(1 - a, 1 - b)
    min1 = min(n - a, n - b)
    print("{} <= k <= {}".format(max1, min1))
    # print("1つめの操作で黒く塗るのは以下")
    for k in range(min(max1, min1), max(max1, min1) + 1):
        print("({},{})".format(a + k, b + k))
        arr.append("{},{}".format(a + k - 1, b + k - 1))
    max2 = max(1 - a, b - n)
    min2 = min(n - a, b - 1)
    print("{} <= k <= {}".format(max2, min2))
    for k in range(min(max2, min2), max(max2, min2) + 1):
        print("({},{})".format(a + k, b - k))
        arr.append("{},{}".format(a + k - 1, b - k - 1))
    return arr


def ccc():
    # l1 = input().split()
    # l2 = input().split()
    l1 = "5 3 2".split()
    l2 = "1 5 1 5".split()
    [n, a, b] = map(lambda x: int(x), l1)
    [p, q, r, s] = map(lambda x: int(x), l2)

    arr = []
    max1 = max(1 - a, 1 - b)
    min1 = min(n - a, n - b)
    print("{} <= k <= {}".format(max1, min1))
    for k in range(min(max1, min1), max(max1, min1) + 1):
        print("({},{})".format(a + k, b + k))
        arr.append("{},{}".format(a + k - 1, b + k - 1))
    max2 = max(1 - a, b - n)
    min2 = min(n - a, b - 1)
    print("{} <= k <= {}".format(max2, min2))
    for k in range(min(max2, min2), max(max2, min2) + 1):
        print("({},{})".format(a + k, b - k))
        arr.append("{},{}".format(a + k - 1, b - k - 1))

    for gyou in range(q - p + 1):
        for nagasa in range(s - r + 1):
            if "{},{}".format(gyou, nagasa) in arr:
                print("#", end="")
            else:
                print(".", end="")
        print()


if __name__ == '__main__':
    # a()
    # b()
    # c()
    # c_g(5, 3, 2)
    ccc()

N = int(input())
A = list(map(int, input().split()[:N]))

# Aに含まれる Number の Counter
# A が [40000 50000 40000] なら 添字40000(Number)の要素が2(Count)になる
# Numberは 1 <= Number <= 99999 のため その範囲のリストを用意
numCntList = [0 for _ in range(100000)]
for i in range(N):
    # AのNumberを先頭から見ていって 見つかった添字(Number)のCountをインクリメント
    numCntList[A[i]] += 1

# 和が100000となる組み合わせが何通り見つかったか
sum100000cnt = 0
# 和が100000になる組み合わせを順に探索  1 + 99999, 2 + 99998, ..., 49999 + 50001
for i in range(1, 50000):
    # 選び方を求めたいのでそれぞれのCount(e.g. 1のCount と 99999のCount)の積を加算
    sum100000cnt += numCntList[i] * numCntList[100000 - i]
# 50000同士の組み合わせを加算 e.g. A が [50000 50000 50000 50000] なら 4C2 (4 * 3) / 2 = 6 を加算
sum100000cnt += numCntList[50000] * (numCntList[50000] - 1) // 2

print(sum100000cnt)

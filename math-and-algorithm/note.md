# ノート

## 問題の概要

1. 省略
2. 省略
3. 省略
4. 省略
5. 省略
6. 省略
7. 省略
8. 省略
9. 省略
10. 階乗 N! Factorial
11. N以下の素数 Prime Numbers
12. Nが素数か判定 Primality Test
13. Nの約数を列挙 Divisor Enumeration
14. Nを素因数分解 e.g. N= 10. 2 5. Factorization
15. AとBの最大公約数 e.g. A=33, B=88. 11. The Greatest Common Divisor
16. N個の正の整数の最大公約数 The Greatest Common Divisor of N Integers
17. N個の正の整数の最小公倍数 The Least Common Multiple of N Integers
18. N個の¥100, ¥200, ¥300, ¥400から2つを選んで合計金額が¥500になる組み合わせの数 Convenience Store 1
    1. Tips ¥500の組み合わせは¥100+¥400, ¥200+¥300のみのためそれぞれの
19. N枚の色付きカードから同じ色を2枚選ぶ方法が何通りあるか Choose Cards 1
20. N枚の整数カードから5枚選び和が1000になる組み合わせが何通りあるか Choose Cards 2
21. 順序を考慮しない組み合わせの数(nCr) Combination Easy
22. N枚の整数カードから2枚選び和が100000となる組み合わせが何通りあるか Choose Cards 3
23. 期待値の和 期待値の線形性 ダイス2個の出目の期待値の和 Dice Expectation
24. 期待値の和 期待値の線形性 選択式問題N問 各配点はQ点 ランダムに回答したときの得点期待値 Answer Exam Randomly
25. 期待値の和 詳細は省略 Jiro's Vacation
26. Coin Gacha

## Tips

### 和の公式

n * (n + 1) / 2

e.g. 1から100までの整数の総和は5050 `100 * 101 / 2 = 5050`

参考: https://white-circle7338.com/1_n_wa/

#### 2乗の総和

n * (n + 1)(2n + 1) / 6

参考: https://w3e.kanazawa-it.ac.jp/math/category/suuretu/suuretu/henkan-tex.cgi?target=/math/category/suuretu/suuretu/siguma-kk.html

### ルートN

- math.sqrt(N)
    - sqrt は square root 平方根
- N ** 0.5

### 小数点以下を切り捨て

- math.floor(N)
- int(N)

### 階乗(N!)

- math.factorial(N)

### 商の切り下げ

- `x // y` e.g. `15 // 2 = 7`

### N行input()

- `P = [map(int, input().split()[:2]) for _ in range(N)]`  
  以下の複数行テキストに対応
  ```text
  2 50
  4 100
  ```

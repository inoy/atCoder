A, B = map(int, input().split())

while A > 0 and B > 0:
    if A > B:
        A = A % B
    else:
        B = B % A
print(A) if A > B else print(B)

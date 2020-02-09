N, A, B = map(int, input().split())
diff = abs(A - B)

if diff % 2 == 0:
    print(diff // 2)

else:
    n = (diff // 2) + 1 + min(N-B, A-1)
    print('N-B, A-1:', N-B, A-1)
    print(n)

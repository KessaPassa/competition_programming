n, k = map(int, input().split())
count = n // k
ans = n - k * count
if abs(ans - k) < ans:
    print(abs(ans - k))
else:
    print(ans)

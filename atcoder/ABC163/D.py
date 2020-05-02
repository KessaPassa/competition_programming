def ncr(n, r):
    if r == 0:
        return 1
    if r == 1:
        return n

    # 4c1と4c3は同じなので小さいrを使う
    r = min(r, n - r)

    # 桁が小さいときは繰り返し二乗法
    if n + r < 4000:
        x, y = 1, 1
        for i in range(r):
            x *= n-i
            y *= i+1
        return x // y

    x = list(range(n - r + 1, n + 1))
    y = list(range(1, r+1))
    for p in range(2, r + 1):
        pivot = y[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p - 1, r, p):
                x[k - offset] //= pivot
                y[k] //= pivot
    result = 1
    for k in range(r):
        result *= x[k]
    return result


n, k = map(int, input().split())
n += 1
MOD = 10**9+7
ans = 0

for i in range(k, n+1):
    ans += ncr(n, i) % MOD
    if i != n and i % 2 == 0:
        ans -= i // 2
print(ans)

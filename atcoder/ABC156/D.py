def nrc_mod(n, r, mod=10**9+7):
    r = min(n - r, r)
    if r == 0:
        return 1

    over = 1
    for i in range(n, n - r, -1):
        over = over * i % mod

    under = 1
    for i in range(1, r + 1):
        under = under * i % mod

    inv = pow(under, mod - 2, mod)
    return over * inv % mod


n, a, b = map(int, input().split())
MOD = 10**9 + 7

# 0本を選ぶは無しなので-1
# 取るか取らないかの２択がn種類ある
ans = pow(2, n, MOD) - 1
ans -= nrc_mod(n, a, MOD)
ans -= nrc_mod(n, b, MOD)
while ans < 0:
    ans += MOD
print(ans)

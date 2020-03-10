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


# # nrc_modよりかなり遅い
# def nrc_mod2(n, r, mod=10**9+7):
#     x, y = 1, 1
#     for i in range(r):
#         x *= (n-i) % mod
#         y *= (i+1) % mod

#     inv = pow(y, mod-2, mod)
#     return x*inv % mod


# 繰り返し二乗法を用いた階乗
def factorial(n):
    if n == 0:
        return 1

    x = factorial(n//2)
    x = x**2

    if n % 2 == 1:
        x *= 2

    return x


# pow(n, p, mod)でも同じことができる
def modpow(n, p, mod=10**9+7):
    if p == 0:
        return 1

    if p % 2 == 0:
        half = modpow(n, p//2, mod)
        return half**2 % mod

    else:
        return n*modpow(n, p-1, mod) % mod


def gcd(a, b):
    if a > b:
        a, b = b, a
    if a == 0:
        return b
    m = b % a
    while m:
        a, b = m, a
        m = b % a
    return a


def lcm(a0, b0):
    if a0 < b0:
        a, b = a0, b0
    else:
        b, a = a0, b0
    if a < 2:
        return b
    m = b % a
    while m:
        a, b = m, a
        m = b % a
    return b0 // a * a0

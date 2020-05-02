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


k = int(input())
ans = 0

for a in range(1, k+1):
    for b in range(1, k+1):
        ab = gcd(a, b)
        for c in range(1, k+1):
            ans += gcd(ab, c)
print(ans)

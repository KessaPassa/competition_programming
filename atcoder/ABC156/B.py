n, k = map(int, input().split())

ans = []
while True:
    q, mod = divmod(n, k)
    ans.append(mod)
    n = q
    if n == 0:
        break

# print(ans[::-1])
print(len(ans))

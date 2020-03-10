n, a, b = map(int, input().split())
ans = n // (a+b)*a
rem = n % (a+b)
ans += min(rem, a)
print(ans)

# if a == 0:
#     print(0)
# elif n <= a or b == 0:
#     print(n)
# elif a < n and n <= a+b:
#     print(a)
# else:
#     mul = n // (a+b)
#     mod = max(n - (mul*a + mul*b), 0)
#     if mod <= a:
#         mod = n - mul*(a+b)
#     else:
#         mod = mod // a * a

#     print(mul*a + mod)

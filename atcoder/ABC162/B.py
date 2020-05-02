a = int(input())

ans = 0
for i in range(1, a+1):
    if not(i % 3 == 0 or i % 5 == 0):
        ans += i
print(ans)

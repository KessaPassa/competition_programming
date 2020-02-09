import sys
sys.setrecursionlimit(1000000000)


def f(n):
    if n < 2:
        return 1
    else:
        return n * f(n-2)


N = int(input())
cal = f(N)

cnt = 0
for c in str(cal)[::-1]:
    if c == '0':
        cnt += 1
    else:
        break
print(cnt)

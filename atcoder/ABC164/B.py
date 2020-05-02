a, b, c, d = map(int, input().split())
while True:
    if c <= 0:
        print('Yes')
        break
    elif a <= 0:
        print('No')
        break
    c -= b
    a -= d

a, b = map(int, input().split())
for yen in range(1, 100*10+1):
    if int(yen * 0.08) == a and int(yen * 0.1) == b:
        print(yen)
        exit()
print(-1)

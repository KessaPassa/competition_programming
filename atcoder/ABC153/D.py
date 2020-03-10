def attack(n):
    if n <= 1:
        return 1

    return 1 + attack(n // 2)*2


h = int(input())
count = attack(h)
print(count)

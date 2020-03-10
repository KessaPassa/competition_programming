h, a = map(int, input().split())
count = h // a
count += 1 if h % a != 0 else 0
print(count)

k = int(input())
a_list = []
for i in range(1, 10):
    a_list.append(i)

while True:
    if k <= len(a_list):
        print(a_list[k-1])
        exit()
    k -= len(a_list)

    old = a_list.copy()
    a_list.clear()
    for x in old:
        for i in [-1, 0, 1]:
            d = x % 10 + i
            if d < 0 or d > 9:
                continue

            nx = x*10+d
            a_list.append(nx)

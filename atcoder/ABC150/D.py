import fractions

n, m = map(int, input().split())
a_list = list(map(int, input().split()))
a_list_half = list(map(lambda x: x//2, a_list))

gcd = a_list_half[0]
for i in range(1, n):
    gcd = fractions.gcd(gcd, a_list_half[i])
# print(gcd)

multi = 1
for a in a_list_half:
    multi *= a
lcm = multi*gcd
# print(lcm)

now_lcm = lcm
result = []
while now_lcm <= m:
    can_div = True
    for a in a_list:
        # print((now_lcm - a*0.5) % a)
        if (now_lcm - a*0.5) % a == 0:
            can_div = True
        else:
            can_div = False

    if can_div:
        result.append(now_lcm)

    now_lcm += lcm
print(len(result))

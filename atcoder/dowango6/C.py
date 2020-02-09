from operator import mul
from functools import reduce


def cmb(n, r):
    r = min(n-r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


n, k = map(int, input().split())
a_list = list(map(int, input().split()))
happiness = [0 for _ in range(n)]
comb_stack = 1

for a in a_list:
    happiness.sort()
    for i in range(a):
        happiness[i] += 1
    c = cmb(n, a)
    comb_stack *= c

multi_happiness = 1
for h in happiness:
    multi_happiness *= h
print((comb_stack * multi_happiness) % (10**9+7))

from fractions import gcd
import sys
sys.setrecursionlimit(100000)

a, b = map(int, input().split())
gcd = gcd(a, b)
if gcd <= 0:
    print(0)
else:
    result = int(a*b / gcd)
    print(result)

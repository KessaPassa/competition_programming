import math
a, b, c = map(int, input().split())
ab_expand = a + 2*(math.sqrt(a*b)) + b
if math.floor(ab_expand) < c < round(ab_expand, 5) or ab_expand < c:
    print('Yes')
else:
    print('No')

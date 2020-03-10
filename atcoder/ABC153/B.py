h, n = map(int, input().split())
a_list = list(map(int, input().split()))

if sum(a_list) >= h:
    print('Yes')
else:
    print('No')

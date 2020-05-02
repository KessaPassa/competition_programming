n, m = map(int, input().split())
a_list = list(map(int, input().split()))
a_list.sort(reverse=True)
if a_list[m-1] < sum(a_list) / (4*m):
    print('No')
else:
    print('Yes')

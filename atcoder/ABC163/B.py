n, m = map(int, input().split())
a_list = list(map(int, input().split()))

if n < sum(a_list):
    print('-1')
else:
    print(n - sum(a_list))

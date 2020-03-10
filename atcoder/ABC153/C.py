n, k = map(int, input().split())
h_list = list(map(int, input().split()))

if len(h_list) <= k:
    print(0)
else:
    h_list.sort(reverse=True)
    for i in range(k):
        h_list[i] = 0
    print(sum(h_list))

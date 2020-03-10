n, m, k = map(int, input().split())
a_list, b_list, c_list, d_list = [], [], [], []
for _ in range(m):
    a, b = map(int, input().split())
    a_list.append(a)
    b_list.append(b)
for _ in range(k):
    c, d = map(int, input().split())
    c_list.append(c)
    d_list.append(d)

friend_dict = {}
for a, b in zip(a_list, b_list):
    if not(a in friend_dict):
        friend_dict[a] = []
    if not(b in friend_dict):
        friend_dict[b] = []

    friend_dict[a].append(b)
    friend_dict[b].append(a)

friend_dict = dict(sorted(friend_dict.items(), key=lambda x: x[0]))

ans_list = []
for key, value in friend_dict.items():
    ans_list.append(n - len(value) - 1)

for c, d in zip(c_list, d_list):
    ans_list[c-1] -= 1
    ans_list[d-1] -= 1
print(' '.join(map(str, ans_list)))

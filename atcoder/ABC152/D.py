def get_first_end(n):
    n = str(n)
    return (int(n[0]), int(n[-1]))


n = int(input())
ans = 0

ans_dict = {}
for i in range(1, n+1):
    p = get_first_end(i)
    if not(p in ans_dict):
        ans_dict[p] = 0
    ans_dict[p] += 1

for i in range(1, n+1):
    p = get_first_end(i)
    reverse = (p[1], p[0])
    if reverse in ans_dict:
        ans += ans_dict[reverse]
print(ans)

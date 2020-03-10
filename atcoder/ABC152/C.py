n = int(input())
p_list = list(map(int, input().split()))

ans = 0
now_min = p_list[0]
for i in range(n):
    # if now_min > p_list[i]:
    #     now_min = p_list[i]
    if p_list[i] <= now_min:
        ans += 1
        now_min = p_list[i]
print(ans)

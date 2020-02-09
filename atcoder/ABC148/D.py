N = int(input())
data = list(map(int, input().split()))

pos_cnt = 1
remove_cnt = 0
for d in data:
    if d == pos_cnt:
        pos_cnt += 1
    else:
        remove_cnt += 1

if remove_cnt == N:
    print(-1)
else:
    print(remove_cnt)

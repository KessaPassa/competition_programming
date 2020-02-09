def search(y, x):
    dy_list = [-1, 0, 1, 0]
    dx_list = [0, -1, 0, 1]

    queue = [(y, x)]
    dist = [[-1 for _ in range(w)] for _ in range(h)]
    dist[y][x] = 0
    while queue:
        # print('queue: ', queue)
        now_y, now_x = queue.pop(0)
        for dy, dx in zip(dy_list, dx_list):
            next_y = now_y+dy
            next_x = now_x+dx

            # 範囲外なら
            if not(0 <= next_y < h and 0 <= next_x < w):
                continue
            # 壁なら
            elif s_list[next_y][next_x] == '#':
                continue
            # 探索済なら
            elif dist[next_y][next_x] != -1:
                continue

            dist[next_y][next_x] = dist[now_y][now_x]+1
            # print((now_y, now_x), (next_y, next_x), dist[now_y][now_x]+1)
            # print(dist, '\n')
            queue.append((next_y, next_x))

    return max(max(d) for d in dist)


h, w = map(int, input().split())
s_list = [list(input()) for _ in range(h)]

ans = 0
for i in range(h):
    for j in range(w):
        if s_list[i][j] == '.':
            ans = max(search(i, j), ans)
print(ans)

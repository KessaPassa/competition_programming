n, x, y = map(int, input().split())
INF = 100100100

# 0から始まる方が扱いやすいのでデクリメント
x -= 1
y -= 1

ans = [0]*n
for sv in range(n):
    dist = [INF]*n
    queue = []

    def push(v, d):
        if dist[v] != INF:
            return
        dist[v] = d
        queue.append(v)
    push(sv, 0)

    while(len(queue) > 0):
        v = queue.pop(0)
        d = dist[v]
        if (v-1) >= 0:
            push(v-1, d+1)
        if (v+1) < n:
            push(v+1, d+1)

        if v == x:
            push(y, d+1)
        if v == y:
            push(x, d+1)

    for i in range(n):
        ans[dist[i]] += 1

# 区別した結果がansに入っている。今回は区別しないので半分にする
for i in range(n):
    ans[i] //= 2
for i in range(n-1):
    print(ans[i])

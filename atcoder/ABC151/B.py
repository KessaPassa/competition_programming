n, k, m = map(int, input().split())
a_list = map(int, input().split())
goal_point = n*m
now_point = sum(a_list)
diff = goal_point - now_point

if diff > k:
    print(-1)
else:
    result_point = diff if diff > 0 else 0
    print(result_point)

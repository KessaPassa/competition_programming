n, k = map(int, input().split())
p_list = list(map(int, input().split()))

scope_index = 0
max_sum = 0
for i in range(k):
    max_sum += p_list[i]

now_sum = max_sum
for p_i in range(k, len(p_list)):
    now_sum -= p_list[p_i - k]
    now_sum += p_list[p_i]

    if max_sum < now_sum:
        scope_index = p_i
        max_sum = now_sum

ex = (max_sum+k)/2
print(ex)

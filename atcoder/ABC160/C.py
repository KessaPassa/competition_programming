import numpy as np

k, n = map(int, input().split())
a_list = list(map(int, input().split()))
a_list.append(k+a_list[0])
diff = list(np.diff(a_list))
diff.remove(max(diff))
print(sum(diff))

# max_dist = 0
# sum_dist = 0
# for i in range(len(a_list)-1):
#     dist = abs(a_list[i+1] - a_list[i])
#     if max_dist < dist:
#         max_dist = dist
#     sum_dist += dist
# sum_dist -= max_dist
# print(sum_dist)

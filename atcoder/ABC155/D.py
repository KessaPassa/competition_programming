import itertools

n, k = list(map(int, input().split()))
a_list = list(map(int, input().split()))
a_list.sort()

comb = list(itertools.combinations(a_list, 2))

ans = []
for c in comb:
    ans.append(c[0]*c[1])
ans.sort()
print(ans[k-1])

# ans_dict = {}
# for i in range(n):
#     for j in range(n):
#         if i == j:
#             continue
#         elif not((i, j) in ans_dict or (j, i) in ans_dict):
#             ans_dict[i, j] = a_list[i]*a_list[j]

# sorted_ans = sorted(ans_dict.items(), key=lambda x: x[1])
# print(sorted_ans)
# print(sorted_ans[k-1][1])

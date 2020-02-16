n = int(input())
s_list = [input() for _ in range(n)]
most_list = []
counter_dict = {}
for s in s_list:
    if s in counter_dict:
        counter_dict[s] += 1
    else:
        counter_dict[s] = 1

sorted_counter = sorted(counter_dict.items(), key=lambda x: x[1], reverse=True)
ans = []
max_num = sorted_counter[0][1]
for c in sorted_counter:
    if max_num == c[1]:
        ans.append(c[0])
    else:
        break

ans.sort()
print('\n'.join(ans))

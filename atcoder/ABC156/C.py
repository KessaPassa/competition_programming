n = int(input())
x_list = list(map(int, input().split()))

x_ave = round(sum(x_list) / len(x_list))
diff_sum = 0
for x in x_list:
    diff = abs(x - x_ave)**2
    diff_sum += diff
print(diff_sum)

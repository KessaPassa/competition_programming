a_list = [list(map(int, input().split())) for _ in range(3)]
n = int(input())
b_list = [int(input()) for _ in range(n)]

for y in range(3):
    for b in b_list:
        if b in a_list[y]:
            index = a_list[y].index(b)
            a_list[y][index] = -1

is_bingo = False
for y in range(3):
    if sum(a_list[y]) == -3:
        is_bingo = True
        break

for x in range(3):
    if a_list[0][x]+a_list[1][x]+a_list[2][x] == -3:
        is_bingo = True
        break

if a_list[0][0]+a_list[1][1]+a_list[2][2] == -3:
    is_bingo = True
elif a_list[0][2]+a_list[1][1]+a_list[2][0] == -3:
    is_bingo = True


if is_bingo:
    print('Yes')
else:
    print('No')

'''
84 97 66
79 89 11
61 59 7
7
89
97
56
79
24
84
30
'''

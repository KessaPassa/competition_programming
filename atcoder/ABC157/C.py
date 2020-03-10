n, m = map(int, input().split())
s_list, c_list = [], []
for _ in range(m):
    s, c = map(int, input().split())
    s_list.append(s)
    c_list.append(str(c))

ans = []
for _ in range(n):
    ans.append('0')

for s, c in zip(s_list, c_list):
    if ans[s-1] == '0':
        ans[s-1] = c
    elif ans[s-1] == c:
        pass
    else:
        print(-1)
        exit()

int_ans = int(''.join(ans))
if len(list(str(int_ans))) == n:
    print(int_ans)
else:
    if not(1 in s_list) and ans[0] == '0':
        ans[0] = '1'
        print(int(''.join(ans)))
    else:
        print(-1)

'''
3 5
1 9
2 1
3 4
3 5
2 9
'''

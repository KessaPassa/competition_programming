a, b = map(int, input().split())

ans = ['', '']
for i in range(b):
    ans[0] += str(a)

b_ans = ''
for i in range(a):
    ans[1] += str(b)

ans.sort()
print(ans[0])

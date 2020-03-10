s = input()
q = int(input())
query_list = [input().split() for _ in range(q)]

front = []
back = []
is_reverse = False

for query in query_list:
    if query[0] == '1':
        is_reverse = not is_reverse
    elif query[0] == '2':
        key = int(query[1])
        value = query[2]
        if (key == 1 and not is_reverse) or (key == 2 and is_reverse):
            front.append(value)
        else:
            back.append(value)

ans = ''
if is_reverse:
    ans = back[::-1]+list(s)[::-1]+front
else:
    ans = front[::-1]+list(s)+back
print(''.join(ans))

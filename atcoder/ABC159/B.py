s = input()
first = s[:len(s)//2]
second = s[len(s)//2+1:]
if first == second:
    print('Yes')
else:
    print('No')

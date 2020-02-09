N = int(input())
S, T = input().split()

result = []
for s, t in zip(S, T):
    result.append(s)
    result.append(t)
print(''.join(result))
import itertools

n = int(input())
p_list = list(map(int, input().split()))
q_list = list(map(int, input().split()))

result = list(itertools.permutations([i for i in range(1, n+1)], n))
# 中身がtuppleなのでlistに変換
result = list(map(lambda x: list(x), result))
a = result.index(p_list)
b = result.index(q_list)
print(abs(a-b))

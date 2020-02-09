class Question:
    def __init__(self, num, result):
        self.num = int(num)
        self.result = result


n, m = map(int, input().split())
p_list = [input().split() for _ in range(m)]
questions = [Question(num, result) for num, result in p_list]

# 高速化のためにsetを使う
ac_list = set()
wa_dict = {}
wa_count = 0

for q in questions:
    if not(q.num in ac_list):
        if q.result == 'AC':
            ac_list.add(q.num)
            wa_count += wa_dict[q.num] if q.num in wa_dict else 0
        elif q.num in wa_dict:
            wa_dict[q.num] += 1
        else:
            wa_dict[q.num] = 1
print('{} {}'.format(len(ac_list), wa_count))

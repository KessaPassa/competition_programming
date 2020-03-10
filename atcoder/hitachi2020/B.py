class SetItem:
    def __init__(self, a, b, sub):
        self.a = a
        self.b = b
        self.sub = sub

    def get_total(self, a_list, b_list):
        a_value = a_list[self.a-1]
        b_value = b_list[self.b-1]
        return a_value + b_value - self.sub


a, b, m = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
set_list = []
for _ in range(m):
    a, b, sub = map(int, input().split())
    set_item = SetItem(a, b, sub)
    set_list.append(set_item.get_total(a_list, b_list))

set_list.sort()
a_list.sort()
b_list.sort()
ans = a_list[0]+b_list[0] if a_list[0]+b_list[0] < set_list[0] else set_list[0]
print(ans)

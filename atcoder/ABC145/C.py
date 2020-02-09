class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def cal_distance(self, pos):
        return ((self.x - pos.x)**2 + (self.y - pos.y)**2)**0.5


N = int(input())
data = [input() for _ in range(N)]

pos_list = []
for d in data:
    x, y = map(int, d.split())
    pos = Pos(x, y)
    pos_list.append(pos)

result_list = []
for i in range(N):
    for j in range(N):
        cal = pos_list[i].cal_distance(pos_list[j])
        result_list.append(cal)

print(sum(result_list) / N)

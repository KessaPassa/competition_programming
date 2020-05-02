# class Network:
#     def __init__(self, color, x, y,):
#         self.color = color
#         self.x = x
#         self.y = y
#         self.right = None
#         self.down = None

#     def set_rihgt(self, right):
#         self.right = right

#     def set_down(self, down):
#         self.down = down


# WHITE = '.'
# BLACK = '#'
# h, w = map(int, input().split())
# s_list = [list(input()) for _ in range(h)]
# network_list = []

# for y in range(h):
#     network_list.append([])
#     for x in range(w):
#         s = s_list[y][x]
#         color = ''
#         if s == '.':
#             color = 'White'
#         elif s == '#':
#             color = 'Black'

#         network = Network(color, x, y)
#         network_list[y].append(network)

# for y in range(h):
#     for x in range(w):
#         n = network_list[y][x]
#         if y < h-1:
#             n.set_down = network_list[y+1][x]
#         else:
#             n.set_dwon = None

#         if x < w-1:
#             n.set_rihgt = network_list[y][x+1]
#         else:
#             n.set_rihgt = None

# n = network_list[0][0]


# ans = 0
# for y in range(h):
#     for x in range(w):
#         pass


# ans = 0
# x, y = 0, 0
# while not((x, y) == (h-1, w-1)):
#     print(y, x)

#     down = s_list[y+1][x]
#     right = s_list[y][x+1]
#     if down == BLACK and right == BLACK:
#         if y < h:
#             x += 1
#         else:
#             y += 1
#     elif down == WHITE:
#         y += 1
#     elif right == WHITE:
#         x += 1
#     else:
#         print('エラー:', y, x)

#     ans += 1
# print(ans)

import heapq


class NeighborList():
    def __init__(self):
        self.neighbor = {}


class Dijkstra(object):
    def dijkstra(self, adj, start, goal=None):
        '''
        ダイクストラアルゴリズムによる最短経路を求めるメソッド
        入力
        adj: adj[i][j]の値が頂点iから頂点jまでの距離(頂点iから頂点jに枝がない場合，値はfloat('inf'))となるような2次元リスト(正方行列)
        start: 始点のID
        goal: オプション引数．終点のID
        出力
        goalを引数に持つ場合，startからgoalまでの最短経路を格納したリストを返す
        持たない場合は，startから各頂点までの最短距離を格納したリストを返す
        '''
        dist = {}  # 始点から各頂点までの最短距離を格納する
        prev = {}  # 最短経路における，その頂点の前の頂点のIDを格納する

        dist[start] = 0
        prev[start] = 0
        # プライオリティキュー．各要素は，(startからある頂点vまでの仮の距離, 頂点vのID)からなるタプル
        q = []
        heapq.heappush(q, (0, start))  # 始点をpush

        while len(q) != 0:
            prov_cost, src = heapq.heappop(q)  # pop

            # プライオリティキューに格納されている最短距離が，現在計算できている最短距離より大きければ，distの更新をする必要はない
            if dist[src] < prov_cost:
                continue

            # 他の頂点の探索
            for dest in adj[src].neighbor.keys():
                cost = adj[src].neighbor[dest]  # src→destのチェック

                if dest in dist.keys():
                    # 先のコスト(仮決定) > 今のコスト+移動するのにかかるコスト
                    if dist[dest] > dist[src] + cost:
                        dist[dest] = dist[src] + cost  # distの更新
                        # キューに新たな仮の距離の情報をpush
                        heapq.heappush(q, (dist[dest], dest))
                        prev[dest] = src                      # 前の頂点IDを記録
                else:  # 訪れたことが無ければ
                    dist[dest] = dist[src] + cost  # distの更新
                    # キューに新たな仮の距離の情報をpush
                    heapq.heappush(q, (dist[dest], dest))
                    prev[dest] = src                      # 前の頂点IDを記録

        if goal is not None:
            return self.get_path(start, goal, prev)
        else:
            return dist

    def get_path(self, start, goal, prev):
        '''
        始点startから終点goalまでの最短経路を求める
        '''
        path = [goal]           # 最短経路
        dest = goal

        # 終点から最短経路を逆順に辿る
        while prev[dest] != start:
            path.append(prev[dest])
            dest = prev[dest]

        path.append(start)

        # 経路をreverseして出力
        return list(reversed(path))


if __name__ == '__main__':
    d = Dijkstra()
    h, w = map(int, input().split())
    s_list = [list(input()) for _ in range(h)]
    n = {}
    for y in range(h):
        for x in range(w):
            n[y, x] = NeighborList()

    # n = {0: NeighborList(), 1: NeighborList(), 2: NeighborList(),
    #      3: NeighborList(), 4: NeighborList()}
    # n[0].neighbor[1] = 2
    # n[0].neighbor[2] = 4

    # n[1].neighbor[0] = 2
    # n[1].neighbor[2] = 3
    # n[1].neighbor[3] = 5

    # n[2].neighbor[0] = 4
    # n[2].neighbor[1] = 3
    # n[2].neighbor[3] = 1
    # n[2].neighbor[4] = 4

    # n[3].neighbor[1] = 5
    # n[3].neighbor[2] = 1
    # n[3].neighbor[4] = 3

    # n[4].neighbor[2] = 4
    # n[4].neighbor[3] = 3

    # result = d.dijkstra(n, 0, 4)
    # print(result)

"""
前処理
"""
import numpy as np
H, N = map(int, input().split())
A = []
B = []
for _ in range(N):
    ai, bi = map(int, input().split())
    """
    入力したものをそれぞれリストに格納していく、これは真似ていこう
    """
    A.append(ai)
    B.append(bi)

"""
配列に変換
"""
A = np.array(A)
B = np.array(B)

"""
処理
"""
# 0からHまで
dp = np.zeros(H+1, dtype=np.int64)
dp[0] = 0

for i in range(1, H+1):
    dp[i] = np.amin(dp[np.maximum(i-A, 0)] + B)

"""
output
"""
print(dp[H])

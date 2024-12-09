# 삼각형 컨베이어 벨트
# https://www.codetree.ai/missions/2/problems/conveyor-belt-triangle?&utm_source=clipboard&utm_medium=text

import sys

n, t = tuple(map(int, sys.stdin.readline().split()))
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]

for _ in range(t):
    temp = arr[2][n - 1]
    for i in range(3):
        temp2 = arr[i][n - 1]
        for j in range(n - 1, 0, -1):
            arr[i][j] = arr[i][j - 1]
        arr[i][0] = temp
        temp = temp2

for i in range(3):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()

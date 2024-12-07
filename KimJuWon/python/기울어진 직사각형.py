# 코드 트리 : 기울어진 직사각형
# 링크 : https://www.codetree.ai/missions/2/problems/slanted-rectangle?&utm_source=clipboard&utm_medium=text

import sys

n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range((n))]


def make_rectangle(n, i, j, arr):
    max_sum = 0
    dx, dy = [1, -1, -1, 1], [1, 1, -1, -1]
    for x in range(1, n):
        temp = arr[i][j]
        if i + x * dx[0] < n and j + x * dy[0] < n:
            for k in range(1, x + 1):
                temp += arr[i + k * dx[0]][j + k * dy[0]]
            new_i = i + x * dx[0]
            new_j = j + x * dy[0]
            for y in range(1, n):
                if new_i + y * dx[1] >= 0 and new_j + y * dy[1] < n:
                    for k in range(1, y + 1):
                        temp += arr[new_i + k * dx[1]][new_j + k * dy[1]]
                    new_i_y = new_i + y * dx[1]
                    new_j_y = new_j + y * dy[1]
                    for z in range(1, n):
                        if new_i_y + z * dx[2] >= 0 and new_j_y + z * dy[2] >= 0:
                            for k in range(1, z + 1):
                                temp += arr[new_i_y + k * dx[2]][new_j_y + k * dy[2]]
                            new_i_z = new_i_y + z * dx[2]
                            new_j_z = new_j_y + z * dy[2]
                            for w in range(1, n):
                                if (
                                    new_i_z + w * dx[3] == i
                                    and new_j_z + w * dy[3] == j
                                ):
                                    for k in range(1, w):
                                        temp += arr[new_i_z + k * dx[3]][
                                            new_j_z + k * dy[3]
                                        ]
                                    max_sum = max(temp, max_sum)
                                    for k in range(1, w):
                                        temp -= arr[new_i_z + k * dx[3]][
                                            new_j_z + k * dy[3]
                                        ]
                            for k in range(1, z + 1):
                                temp -= arr[new_i_y + k * dx[2]][new_j_y + k * dy[2]]
                    for k in range(1, y + 1):
                        temp -= arr[new_i + k * dx[1]][new_j + k * dy[1]]
            for k in range(1, x + 1):
                temp -= arr[i + k * dx[0]][j + k * dy[0]]

    return max_sum


max_sum = 0
for i in range(n):
    for j in range(n):
        max_sum = max(max_sum, make_rectangle(n, i, j, arr))


print(max_sum)

# 1차원 바람
# https://www.codetree.ai/missions/2/problems/The-1D-wind-blows?&utm_source=clipboard&utm_medium=text

import sys

n, m, q = tuple(map(int, sys.stdin.readline().split()))
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
winds = [tuple(sys.stdin.readline().split()) for _ in range(q)]


def check_b(r, arr, n, m):
    if r - 1 >= 0:
        for i in range(m):
            if arr[r - 1][i] == arr[r][i]:
                return True
    return False


def check_u(r, arr, n, m):
    if r + 1 < n:
        for i in range(m):
            if arr[r + 1][i] == arr[r][i]:
                return True
    return False


for wind in winds:
    u_done = False
    b_done = False

    r, d = int(wind[0]) - 1, wind[1]
    u_d = ""
    b_d = ""
    if d == "L":
        temp = arr[r][m - 1]
        for i in range(m - 1, 0, -1):
            arr[r][i] = arr[r][i - 1]
        arr[r][0] = temp
        u_d = "R"
        b_d = "R"
    elif d == "R":
        temp = arr[r][0]
        for i in range(m - 1):
            arr[r][i] = arr[r][i + 1]
        arr[r][m - 1] = temp
        u_d = "L"
        b_d = "L"

    u_done = check_u(r, arr, n, m)
    b_done = check_b(r, arr, n, m)
    u = r + 1
    b = r - 1

    while u_done is True:
        if u_d == "L":
            temp = arr[u][m - 1]
            for i in range(m - 1, 0, -1):
                arr[u][i] = arr[u][i - 1]
            arr[u][0] = temp
            u_d = "R"
        elif u_d == "R":
            temp = arr[u][0]
            for i in range(m - 1):
                arr[u][i] = arr[u][i + 1]
            arr[u][m - 1] = temp
            u_d = "L"

        u_done = check_u(u, arr, n, m)
        u += 1

    while b_done is True:
        if b_d == "L":
            temp = arr[b][m - 1]
            for i in range(m - 1, 0, -1):
                arr[b][i] = arr[b][i - 1]
            arr[b][0] = temp
            b_d = "R"

        elif b_d == "R":
            temp = arr[b][0]
            for i in range(m - 1):
                arr[b][i] = arr[b][i + 1]
            arr[b][m - 1] = temp
            b_d = "L"
        # print(b_d)
        b_done = check_b(b, arr, n, m)
        b -= 1


for i in range(n):
    for j in range(m):
        print(arr[i][j], end=" ")
    print()

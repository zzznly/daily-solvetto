# 최단 Run Length 인코딩
# https://www.codetree.ai/missions/2/problems/shortest-run-length-encoding?&utm_source=clipboard&utm_medium=text

import sys

a = sys.stdin.readline().rstrip()
n = len(a)
answer = sys.maxsize

for _ in range(n):
    temp = f"{a[0]}"
    checker = 1
    for i in range(1, n):
        if a[i - 1] != a[i]:
            temp += str(checker)
            temp += a[i]
            checker = 1
        else:
            checker += 1
    temp += str(checker)
    answer = min(len(temp), answer)
    last = a[-1]
    without_last = a[:-1]
    a = a[-1] + a[:-1]

print(answer)

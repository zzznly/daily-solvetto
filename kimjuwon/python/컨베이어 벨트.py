# 컨베이어 벨트
# https://www.codetree.ai/missions/2/problems/conveyor-belt?&utm_source=clipboard&utm_medium=text

import sys
from collections import deque

n, t = tuple(map(int, sys.stdin.readline().split()))
deque1 = deque(list(map(int, sys.stdin.readline().split())))
deque2 = deque(list(map(int, sys.stdin.readline().split())))

for _ in range(1, t + 1):
    deque1.appendleft(deque2.pop())
    deque2.appendleft(deque1.pop())

for ele in deque1:
    print(ele, end=" ")
print()
for ele in deque2:
    print(ele, end=" ")

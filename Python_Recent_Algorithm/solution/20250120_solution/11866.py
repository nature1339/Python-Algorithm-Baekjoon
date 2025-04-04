import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
dq = deque([i for i in range(1, n + 1)])
res = []

while dq:
    for i in range(k - 1):
        dq.append(dq.popleft())
    res.append(dq.popleft())

print('<', ', '.join(list(map(str, res))), '>', sep='')
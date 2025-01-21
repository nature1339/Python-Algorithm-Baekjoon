import sys

input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))
p.sort()

res = 0
for i in range(n):
    res += sum(p[0 : i + 1])
print(res)


# # - 문제 카드 2

# from collections import deque

# n = int(input())
# dq = deque(range(1, n + 1))

# while len(dq) > 1:
#     dq.popleft()
#     dq.append(dq.popleft())

# print(dq[0])

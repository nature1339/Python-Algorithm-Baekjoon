import sys
input = sys.stdin.readline

n = int(input())
rope = []
res = 0
for i in range(n):
    rope.append(int(input()))
rope.sort(reverse=True)

for i in range(n):
    res = max(res, rope[i] * (i + 1))
print(res)
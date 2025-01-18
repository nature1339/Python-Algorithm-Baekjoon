import sys

sys.stdin = open("input_11659.txt")
readl = sys.stdin.readline


n, m = map(int, readl().split())  # 5  3
arr = list(map(int, readl().rstrip()))  # 5 4 3 2 1
pre = [0]
for x in arr:
    pre.append(pre[-1] + x)

for _ in range(m):
    i, j = map(int, readl().split())
    print(pre[j] - pre[i - 1])

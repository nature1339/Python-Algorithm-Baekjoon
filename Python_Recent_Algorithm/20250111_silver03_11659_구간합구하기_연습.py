import sys

sys.stdin = open("input_11659.txt")
readl = sys.stdin.readline

n, m = map(int, readl().split())  # 5 4 3 2 1

arr = list(map(int, readl().split()))
pre = [0]  # [0 5 9 12 14 15]
for x in arr:
    pre.append[pre[-1] + x]

for _ in range(m):  # 3 세번을 돌면서
    i, j = map(int, readl().split())  # 불러옴 1 3
    print(pre[j] - pre[i - 1])

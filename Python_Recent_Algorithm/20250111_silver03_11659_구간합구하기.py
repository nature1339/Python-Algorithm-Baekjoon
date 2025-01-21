import sys

sys.stdin = open("input_11659.txt")
readl = sys.stdin.readline

n, m = map(int, readl().split())  # 5  3
# 5 4 3 2 1
# arr = map(int, readl().split()) # error
arr = list(map(int, readl().split()))  # 5 4 3 2 1

pre = [0]  # 0 5 9 12 14 15
#              5 4  3  2  1
for x in arr:
    pre.append(pre[-1] + x)
# [0]
# [0 5]
# [0 5 9]
# ...
# [0 5 9 12 14 15]
#  0 1 2 3  4  5

for _ in range(m):
    # i번째, j번째
    # 1 3
    # pre[3] - pre[0]
    i, j = map(int, readl().split())
    print(pre[j] - pre[i - 1])

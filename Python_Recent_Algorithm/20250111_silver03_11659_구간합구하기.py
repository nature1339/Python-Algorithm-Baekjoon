import sys

sys.stdin = open("input_11659.txt")
readl = sys.stdin.readline


n, m = readl().split()  # 5  3
n_list = readl().rstrip()  # 5 4 3 2 1
sum = 0

for k in range(m):  # 3
    i, j = readl().rstrip()  # 1 3 -> 1 2 3
    for _ in range(i, j):  #  5 4 3
        sum += i + j
    print(sum)


# print(n + m)

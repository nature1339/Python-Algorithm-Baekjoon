import sys

sys.stdin = open("input_11659.txt")
readl = sys.stdin.readline

n, m = map(int, readl().split())  # 5 4 3 2 1

arr = list[readl().split()]
s = [0]  # [0 5 9 12 14 15]

for i, j in range(m):  # 3 세번을 돌면서
    m = readl().split()  # 불러옴 1 3
    ans = s[j] - s[i]

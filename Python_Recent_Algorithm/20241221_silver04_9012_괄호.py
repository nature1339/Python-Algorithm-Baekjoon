import sys

sys.stdin = open("input_9012.txt")
readl = sys.stdin.readline

n = int(readl())  # 6

# (()(()))

pa = [readl().rstrip() for i in range(n)]

# (())())
if pa[i] == "(":
    pa

import sys
sys.stdin = open('input_1544.txt')
readl = sys.stdin.readline


n = int(readl().rstrip())

s = set([readl().rstrip() for i in range(n)])

print(len(s))




import sys
sys.stdin = open('input_1269.txt')
readl = sys.stdin.readline



n, m = map(int((readl())))
a = set(int(readl())) #1 2 4
b = set(int(readl()))

c = list(a-b)
print(len(c))
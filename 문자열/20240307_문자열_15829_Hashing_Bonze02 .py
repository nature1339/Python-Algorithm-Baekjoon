import sys
sys.stdin = open('input_15829.txt')
readl = sys.stdin.readline

L = int(readl())
line = readl().rstrip()

r, M = 31, 1234567891

H = 0
for i in range(L):
    a = ord(line[i]) - ord('a') + 1
    H += a * (r ** i)
    H %= M
print(H)
    
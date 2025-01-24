import sys

# input = sys.stdin.readline
sys.stdin = open("input_11399.txt")

n = int(input())
p = list(map(int, input().split()))  # 3 1 4 3 2
p.sort()
res = 0  # 누적합

for i in range(n):
    res += sum(p[0 : i + 1])
print(res)

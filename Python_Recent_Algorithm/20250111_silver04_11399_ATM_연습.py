import sys

# input = sys.stdin.readline
sys.stdin = open("input_11399.txt")
readl = sys.stdin.readline

n = int(input())
s = list(map(int, readl().split()))  # 3 1 4 3 2
pre = [0]  # 누적합
"""
[0 3 1 4 3 2]
[0]
[0 3]
[0 3 4]
[0 3 4 8]
"""
#  s = 3 1 4 3 2
for i in s:
    pre[i] = s[i - 1] + s[i]
    pre.append(pre[i])  #
print(pre)
#     if new[i] > new[i + 1]:
#         new[i + 1] = new[i]
# print(new)

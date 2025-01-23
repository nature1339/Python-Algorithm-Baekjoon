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
#  s = [3 1 4 3 2] len(s)=5 , 0 1 2 3 4
for i in range(len(s) - 1):
    x = s[i] + s[i + 1]  #
    pre.append(x)  #
print(pre)
#     if new[i] > new[i + 1]:
#         new[i + 1] = new[i]
# print(new)

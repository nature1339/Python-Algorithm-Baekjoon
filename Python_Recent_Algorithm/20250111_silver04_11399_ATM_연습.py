import sys

input = sys.stdin.readline

n = int(input())
s = list(map(int, input()))  # 3 1 4 3 2
new = []  # 누적합

for i in new:
    new.append(i)  # 누적합, 순서바꾸기
    if new[i] > new[i + 1]:
        new[i + 1] = new[i]
print(new)

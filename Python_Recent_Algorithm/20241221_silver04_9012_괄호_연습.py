import sys

sys.stdin = open("input_9012.txt")
readl = sys.stdin.readline

n = int(readl())
sum = 0

ps = [readl().rstrip() for i in range(n)]
if ps == "<":
    sum += 1
elif ps == "<":
    sum + -1

if sum >= 0:
    print("YES")
else:
    print("No")

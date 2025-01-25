import sys
input = sys.stdin.readline

k = int(input())
l = []
while k:
    n = int(input())
    if n == 0:
        l.pop()
    else:
        l.append(n)
    k -= 1
print(sum(l))
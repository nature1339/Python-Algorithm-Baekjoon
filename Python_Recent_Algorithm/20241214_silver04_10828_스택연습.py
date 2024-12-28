import sys

sys.stdin = open("input_10828.txt")
readl = sys.stdin.readline

n = int(readl())
s = []

for _ in range(n):
    inputs = readl().split()  # push 1
    word = inputs[0]

    if word == "push":
        num = inputs[1]
        s.append(num)

    elif word == "pop":
        if s:
            print(s.pop())
        else:
            print(-1)

    elif word == "size":
        print(len(s))

    elif word == "empty":
        if s:
            print(0)
        else:
            print(1)

    elif word == "top":
        if s:
            print(s[-1])
        else:
            print(-1)

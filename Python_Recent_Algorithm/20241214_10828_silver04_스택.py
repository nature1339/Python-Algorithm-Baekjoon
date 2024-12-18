import sys

sys.stdin = open("input_10828.txt")
readl = sys.stdin.readline

n = int(readl())
s = []

# for i in range(n):
#     word = readl().split()
#     print(word)
#     num = word[1]  --> ['push', '1']
# ['push', '2']
# ['top']  -> 뒤에 word[1]에 숫자없어서 에러

for _ in range(n):
    inputs = readl().split()  # push 1 # 한줄에 여러단어-> split
    word = inputs[0]

    if word == "push":
        num = inputs[1]  # push
        s.append(num)  # 1

    elif word == "top":
        # if len(s) != 0:
        if s:
            print(s[-1])
        else:
            print(-1)

    elif word == "size":
        print(len(s))

    elif word == "pop":
        # if len(s) != 0:
        if s:
            print(s.pop())  # 맨뒤에거 꺼내서 출력
        else:
            print(-1)

    elif word == "empty":
        # if len(s) != 0:
        if s:  # stack 에 뭐가 있으면
            print(0)
        else:
            print(1)

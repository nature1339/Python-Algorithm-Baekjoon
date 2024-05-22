import sys
sys.stdin = open('input_9093.txt')
readl = sys.stdin.readline

# 2
# I am happy today
# We want to win the first prize

n = int(readl()) #2

for i in range(n): #2
    line = readl().split()   #'I am happy today'-> ['I', 'am', 'happy', 'today']
                             # split은 리스트로 들어간다.

    for j in range(len(line)):   # ['I', 'am', 'happy', 'today'] #문자열은 인덱스로 접근만 가능
        line[j] = line[j][::-1]   # I ma yppah yadot
    print(' '.join(line))            # line[0]  line[1]  line[2]   
                           # I[::-1] am[::-1]
                           #  I       ma 
    
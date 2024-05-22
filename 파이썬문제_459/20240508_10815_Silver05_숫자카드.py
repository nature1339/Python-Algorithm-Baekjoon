import sys
sys.stdin = open('input_10815.txt')
readl = sys.stdin.readline

n = int(readl()) # 상근이가 가지고 있는 숫자 카드의 개수 N
line = set(readl().split()) #6 3 2 10 -10

m = int(readl())
all = readl().split() #10 9 -5 2 3 4 5 -10

have = []

for j in all: #8
    if j in line:  # list -> 500,000  set -> 1            
        j = 1
        have.append(j)
    else:
        j = 0 
        have.append(j)
print(" ".join(map(str, have)))           
         
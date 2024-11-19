import sys
sys.stdin = open('input_1302.txt')
readl = sys.stdin.readline

n = int(readl())
qty = {} #top:1, kimtop:1

for i in range(n):
     qty.key= readl().rstrip() # top, top , kimtop
     if qty.key >= 1:
        qty.value += 1

for value in qty.values:
    if value == value:
        value.sort
    best = max(qty.value) 

print(best)
    
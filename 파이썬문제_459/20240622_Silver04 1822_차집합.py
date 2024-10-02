import sys
sys.stdin = open('input_1822.txt')
readl = sys.stdin.readline

n, m = map(int, readl().split())

a = list(map(int, readl().split())) #[2, 5, 11, 7]
b = list(map(int, readl().split())) #[9, 7, 4]
c = []

for i in range(n):# [2, 5, 11, 7]
    if i in a and b :
        c.append(i)
print(c)        
        

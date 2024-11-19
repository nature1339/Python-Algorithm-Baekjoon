import sys
sys.stdin = open('input_1977.txt')
readl = sys.stdin.readline

p = [] #64 81 100
x = 1
sum = 0
m = int(readl().rstrip())
n = int(readl().rstrip())  #60 100

for x in range(101):
    if x**2 > n:
        break
    if m<= (x**2) <= n:
        p.append(x**2)
        sum += x**2    #p[0]+p[1]+p[2]

if len(p) == 0:  # not p:
    print(-1)
else:
    print(sum)
    print(p[0])
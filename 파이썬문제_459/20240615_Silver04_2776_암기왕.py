import sys
sys.stdin = open('input_2776.txt')
readl = sys.stdin.readline

t = int(readl())

su1 = []
su2 = []

for i in range(t):
    n = int(readl().rstrip()) #5
    for j in range(n): #5
        su1 = map(int,readl().split()) #4 1 5 2 3
    m = int(readl().rstrip()) #5
    for j in range(m): #5
        su2 = map(int,readl().split()) #1 3 7 9 5
for i in su2:
    if i in su2:       
        print("1")
    else: 
        print("0")

import sys
sys.stdin = open('input_9575.txt')
readl = sys.stdin.readline

n = int(readl())

def lucky(num):
    while True:
        r,m = a // 5 and a % 8 == 0
    

for i in range(n):
    a_n = readl()
    a = map(int, readl().split) #100 1 10 100 1 1
    b_n = readl()
    b = map(int, readl().split) #3 53 53 53 53 53 53
    c_n = readl()
    c = map(int, readl().split) #4 54 4 54 4 54

lucky = []

for i in range(a):  #100 1 10 100 1 1       100
    for j in range(b): #3 53 53 53 53 53 53   3
        for k in range(c): #4 54 4 54 4 54     4
            if (a+b+c) % 5 == 0 or (a+b+c) % 8 == 0: #행운의수
                lucky.append(a,b,c)
print(lucky)                

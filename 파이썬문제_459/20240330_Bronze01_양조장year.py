import sys
sys.stdin = open('input_11557.txt')
readl = sys.stdin.readline

t = int(readl())
m = []  #Yonsei, 10 , x,y
# 2
# 3
# Yonsei 10
# Korea 10000000
# Ewha 20
for i in range(t): #2, i = 0일때, j = 0    
    n = int(readl().rstrip())
    
    Max = -1  # 10000000
    name = ''  # Korea
    for j in range(n): #i = 0, j= 0,1,2        
        x, y = readl().split()   #Ewha 20
        y = int(y)
        
        if y > Max:
            Max = y # 10000000
            name = x # Korea
    print(name)
        # print(x)
#         m.append(y)
#     print(key(max(m)))
    
# h = [3, 4, 9, 7, 4, 5, 9, ...]
# max = 0
# for x in h:
#     if x > max:
#         max = x
# for i in range(n):
# if i > i-1:
#     print(i)

        
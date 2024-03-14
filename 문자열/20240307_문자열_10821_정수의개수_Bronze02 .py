import sys
sys.stdin = open('input_10821.txt')
readl = sys.stdin.readline

# 10,20,30,50,100

# line = list[readl().rstrip()] #10,20,30,50,100 

line = readl().split(',') # 10 20 30 50 100
# c v b n m
# ['c', 'v', 'b', 'n', 'm']

print(len(line))

# # len(line)     # [-1]
# for i , ch in enumerate(readl()): #10,20,30,50,100 
#     #i = 0 , ch=10
#     if  int(ch) >= 0: 
#         l.append(i)
#     if  int(ch) < 0:   
#         l.append(i)
#         # 정수 = 양수, 0, 음수 
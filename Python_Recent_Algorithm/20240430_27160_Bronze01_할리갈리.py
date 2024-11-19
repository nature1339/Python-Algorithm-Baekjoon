import sys
sys.stdin = open('input_27160.txt')
readl = sys.stdin.readline

num = int(readl())
count = 0

s = ['strawberry', 'banana', 'lime', 'plum']
# 3
# BANANA 2
# PLUM 4
# BANANA 3

for i in range(num): 
    name, fruit_num = readl().split() #BANANA 2
    for j in s:
        if name == j:  #banana = banana
            count += fruit_num
if count == 5:
    print('YES')
else:
    print('NO')    
        
        